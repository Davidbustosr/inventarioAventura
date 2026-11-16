from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from cuentas.forms import PerfilForm, RegistroForm, UsuarioEditarForm
from cuentas.models import Perfil


# ---------------------------------------------------------------
# LOGIN Y LOGOUT (manejo de sesiones)
# ---------------------------------------------------------------
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate revisa si el usuario y la contraseña existen en la BD
        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)  # crea la SESION (tabla django_session + cookie sessionid)

            # Si el usuario no tiene perfil (ej: creado con createsuperuser) se lo creamos
            perfil, creado = Perfil.objects.get_or_create(usuario=usuario)
            if usuario.is_superuser:
                perfil.rol = 'ADMIN'
                perfil.save()

            # Guardamos datos en la sesion para usarlos en todas las paginas
            request.session['rol'] = perfil.rol
            request.session['nombre'] = usuario.first_name + ' ' + usuario.last_name
            request.session['hora_ingreso'] = timezone.localtime().strftime('%d-%m-%Y %H:%M')
            request.session['vistas_recientes'] = []

            if not request.POST.get('recordarme'):
                request.session.set_expiry(0)  # la sesion se borra al cerrar el navegador

            messages.success(request, 'Bienvenido/a ' + request.session['nombre'])
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'registration/login.html')


def cerrar_sesion(request):
    if request.method == 'POST':
        logout(request)  # borra toda la sesion
        messages.info(request, 'Sesión cerrada')
    return HttpResponseRedirect(reverse('inicio'))


def registro(request):
    """Crear cuenta: todo el que se registra queda como TURISTA."""
    form = RegistroForm()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(usuario=usuario, rol='TURISTA')
            messages.success(request, 'Cuenta creada, ahora inicia sesión')
            return HttpResponseRedirect(reverse('login'))
    data = {'form': form}
    return render(request, 'registration/signup.html', data)


@login_required
def mi_perfil(request):
    perfil = Perfil.objects.get(usuario=request.user)
    data = {'perfil': perfil}
    return render(request, 'cuentas/mi_perfil.html', data)


# ---------------------------------------------------------------
# CRUD DE USUARIOS (solo ADMINISTRADOR)
# ---------------------------------------------------------------
@login_required
def listar_usuarios(request):
    if request.session.get('rol') != 'ADMIN':  # validamos el rol guardado en la sesion
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    usuarios = User.objects.all().order_by('id')  # SELECT * FROM auth_user
    data = {'usuarios': usuarios}
    return render(request, 'cuentas/usuarios.html', data)


@login_required
def crear_usuario(request):
    if request.session.get('rol') != 'ADMIN':  # validamos el rol guardado en la sesion
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    form = RegistroForm()
    perfil_form = PerfilForm()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        perfil_form = PerfilForm(request.POST)
        if form.is_valid() and perfil_form.is_valid():
            usuario = form.save()
            perfil = perfil_form.save(commit=False)  # todavia no lo guarda en la BD
            perfil.usuario = usuario                 # le asignamos el usuario recien creado
            perfil.save()
            messages.success(request, 'Usuario creado')
            return HttpResponseRedirect(reverse('listar_usuarios'))
    data = {'form': form, 'perfil_form': perfil_form, 'titulo': 'Nuevo usuario'}
    return render(request, 'cuentas/usuario_form.html', data)


@login_required
def editar_usuario(request, id):
    if request.session.get('rol') != 'ADMIN':  # validamos el rol guardado en la sesion
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    usuario = get_object_or_404(User, id=id)
    perfil, creado = Perfil.objects.get_or_create(usuario=usuario)
    form = UsuarioEditarForm(instance=usuario)
    perfil_form = PerfilForm(instance=perfil)
    if request.method == 'POST':
        form = UsuarioEditarForm(request.POST, instance=usuario)
        perfil_form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid() and perfil_form.is_valid():
            form.save()
            perfil_form.save()
            messages.success(request, 'Usuario actualizado')
            return HttpResponseRedirect(reverse('listar_usuarios'))
    data = {'form': form, 'perfil_form': perfil_form, 'titulo': 'Editar usuario ' + usuario.username}
    return render(request, 'cuentas/usuario_form.html', data)


@login_required
def eliminar_usuario(request, id):
    if request.session.get('rol') != 'ADMIN':  # validamos el rol guardado en la sesion
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        if usuario == request.user:
            messages.error(request, 'No puedes eliminar tu propia cuenta')
        else:
            usuario.delete()
            messages.success(request, 'Usuario eliminado')
    return HttpResponseRedirect(reverse('listar_usuarios'))
