from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from experiencias.forms import CategoriaForm, ExperienciaForm
from experiencias.models import Categoria, Experiencia, Inscripcion


# ===============================================================
# CRUD CATEGORIAS (solo ADMINISTRADOR)
# ===============================================================
@login_required
def listar_categorias(request):
    if request.session.get('rol') != 'ADMIN':
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    categorias = Categoria.objects.all().order_by('id')  # SELECT * FROM categoria
    data = {'categorias': categorias}
    return render(request, 'experiencias/categorias.html', data)


@login_required
def crear_categoria(request):
    if request.session.get('rol') != 'ADMIN':
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    form = CategoriaForm()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()  # INSERT
            messages.success(request, 'Categoría creada')
            return HttpResponseRedirect(reverse('listar_categorias'))
    data = {'form': form, 'titulo': 'Nueva categoría'}
    return render(request, 'experiencias/categoria_form.html', data)


@login_required
def editar_categoria(request, id):
    if request.session.get('rol') != 'ADMIN':
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(instance=categoria)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()  # UPDATE (porque tiene instance)
            messages.success(request, 'Categoría actualizada')
            return HttpResponseRedirect(reverse('listar_categorias'))
    data = {'form': form, 'titulo': 'Editar categoría'}
    return render(request, 'experiencias/categoria_form.html', data)


@login_required
def eliminar_categoria(request, id):
    if request.session.get('rol') != 'ADMIN':
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        try:
            categoria.delete()  # DELETE
            messages.success(request, 'Categoría eliminada')
        except ProtectedError:
            # on_delete=PROTECT no deja borrar una categoria que tiene experiencias
            messages.error(request, 'No se puede eliminar: tiene experiencias asociadas')
    return HttpResponseRedirect(reverse('listar_categorias'))


# ===============================================================
# GESTION DE EXPERIENCIAS (ADMIN ve todas, GUIA solo las suyas)
# ===============================================================
@login_required
def listar_experiencias(request):
    rol = request.session.get('rol')
    if rol == 'ADMIN':
        experiencias = Experiencia.objects.all()
    elif rol == 'GUIA':
        experiencias = Experiencia.objects.filter(creador=request.user)  # solo las del guia
    else:
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    data = {'experiencias': experiencias}
    return render(request, 'experiencias/experiencias.html', data)


@login_required
def crear_experiencia(request):
    if request.session.get('rol') not in ['ADMIN', 'GUIA']:
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    form = ExperienciaForm()
    if request.method == 'POST':
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            experiencia = form.save(commit=False)  # crea el objeto sin guardarlo aun
            experiencia.creador = request.user      # el creador es el usuario de la sesion
            experiencia.save()                      # ahora si: INSERT
            messages.success(request, 'Experiencia creada')
            return HttpResponseRedirect(reverse('listar_experiencias'))
    data = {'form': form, 'titulo': 'Nueva experiencia'}
    return render(request, 'experiencias/experiencia_form.html', data)


@login_required
def editar_experiencia(request, id):
    rol = request.session.get('rol')
    if rol == 'ADMIN':
        experiencia = get_object_or_404(Experiencia, id=id)
    elif rol == 'GUIA':
        # El guia solo puede editar las suyas: si no es suya -> error 404
        experiencia = get_object_or_404(Experiencia, id=id, creador=request.user)
    else:
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    form = ExperienciaForm(instance=experiencia)
    if request.method == 'POST':
        form = ExperienciaForm(request.POST, instance=experiencia)
        if form.is_valid():
            form.save()  # UPDATE
            messages.success(request, 'Experiencia actualizada')
            return HttpResponseRedirect(reverse('listar_experiencias'))
    data = {'form': form, 'titulo': 'Editar experiencia'}
    return render(request, 'experiencias/experiencia_form.html', data)


@login_required
def eliminar_experiencia(request, id):
    if request.session.get('rol') != 'ADMIN':  # el GUIA no puede eliminar
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    experiencia = get_object_or_404(Experiencia, id=id)
    if request.method == 'POST':
        experiencia.delete()  # DELETE (y por CASCADE se borran sus inscripciones)
        messages.success(request, 'Experiencia eliminada')
    return HttpResponseRedirect(reverse('listar_experiencias'))


@login_required
def inscritos_experiencia(request, id):
    """Detalle del grupo: los turistas inscritos en una experiencia."""
    rol = request.session.get('rol')
    if rol == 'ADMIN':
        experiencia = get_object_or_404(Experiencia, id=id)
    elif rol == 'GUIA':
        experiencia = get_object_or_404(Experiencia, id=id, creador=request.user)
    else:
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    inscripciones = Inscripcion.objects.filter(experiencia=experiencia)
    data = {'experiencia': experiencia, 'inscripciones': inscripciones}
    return render(request, 'experiencias/inscritos.html', data)


# ===============================================================
# CATALOGO Y RESERVAS DEL TURISTA
# ===============================================================
@login_required
def catalogo(request):
    # Solo experiencias activas, de categorias activas y con fecha futura
    experiencias = Experiencia.objects.filter(activa=True, categoria__activo=True,
                                              fecha__gte=timezone.now())

    categoria_id = request.GET.get('categoria')  # filtro opcional: ?categoria=1
    if categoria_id:
        experiencias = experiencias.filter(categoria_id=categoria_id)

    # Lista guardada en la SESION con las ultimas experiencias vistas
    ids_vistas = request.session.get('vistas_recientes', [])
    vistas = Experiencia.objects.filter(id__in=ids_vistas)

    # ids de las experiencias que este usuario ya reservo
    mis_ids = []
    for inscripcion in Inscripcion.objects.filter(usuario=request.user):
        mis_ids.append(inscripcion.experiencia.id)

    data = {
        'experiencias': experiencias,
        'categorias': Categoria.objects.filter(activo=True),
        'categoria_id': categoria_id,
        'vistas': vistas,
        'mis_ids': mis_ids,
    }
    return render(request, 'experiencias/catalogo.html', data)


@login_required
def detalle_experiencia(request, id):
    experiencia = get_object_or_404(Experiencia, id=id)

    # Agregamos esta experiencia a la lista de la sesion (maximo 4, sin repetir)
    vistas = request.session.get('vistas_recientes', [])
    if id in vistas:
        vistas.remove(id)
    vistas.insert(0, id)
    request.session['vistas_recientes'] = vistas[:4]

    ya_inscrito = Inscripcion.objects.filter(usuario=request.user, experiencia=experiencia).first()
    data = {'experiencia': experiencia, 'ya_inscrito': ya_inscrito}
    return render(request, 'experiencias/detalle.html', data)


@login_required
def reservar(request, id):
    if request.session.get('rol') != 'TURISTA':
        messages.error(request, 'Solo los turistas pueden reservar')
        return HttpResponseRedirect(reverse('dashboard'))
    experiencia = get_object_or_404(Experiencia, id=id)
    if request.method == 'POST':
        if Inscripcion.objects.filter(usuario=request.user, experiencia=experiencia).exists():
            messages.warning(request, 'Ya estás inscrito en esta experiencia')
        elif experiencia.cupos_disponibles() <= 0:
            messages.error(request, 'No quedan cupos disponibles')
        else:
            Inscripcion.objects.create(usuario=request.user, experiencia=experiencia)  # INSERT
            messages.success(request, 'Reserva creada, queda pendiente de pago')
            return HttpResponseRedirect(reverse('mis_reservas'))
    return HttpResponseRedirect(reverse('detalle_experiencia', args=[id]))


@login_required
def mis_reservas(request):
    if request.session.get('rol') != 'TURISTA':
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    reservas = Inscripcion.objects.filter(usuario=request.user)  # solo las del turista
    data = {'reservas': reservas}
    return render(request, 'experiencias/mis_reservas.html', data)


@login_required
def pagar_reserva(request, id):
    # usuario=request.user: solo puede pagar SUS reservas (si no es suya -> 404)
    reserva = get_object_or_404(Inscripcion, id=id, usuario=request.user)
    if request.method == 'POST':
        reserva.estado_pago = 'CONFIRMADO'
        reserva.save()  # UPDATE
        messages.success(request, 'Pago confirmado')
    return HttpResponseRedirect(reverse('mis_reservas'))


@login_required
def cancelar_reserva(request, id):
    reserva = get_object_or_404(Inscripcion, id=id, usuario=request.user)
    if request.method == 'POST':
        if reserva.estado_pago == 'CONFIRMADO':
            messages.error(request, 'Una reserva pagada no se puede cancelar')
        else:
            reserva.delete()  # DELETE
            messages.success(request, 'Reserva cancelada')
    return HttpResponseRedirect(reverse('mis_reservas'))


# ===============================================================
# TODAS LAS RESERVAS (solo ADMINISTRADOR)
# ===============================================================
@login_required
def listar_reservas(request):
    if request.session.get('rol') != 'ADMIN':
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    reservas = Inscripcion.objects.all().order_by('-fecha_inscripcion')
    data = {'reservas': reservas}
    return render(request, 'experiencias/reservas.html', data)


@login_required
def cambiar_estado_reserva(request, id):
    if request.session.get('rol') != 'ADMIN':
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    reserva = get_object_or_404(Inscripcion, id=id)
    if request.method == 'POST':
        if reserva.estado_pago == 'PENDIENTE':
            reserva.estado_pago = 'CONFIRMADO'
        else:
            reserva.estado_pago = 'PENDIENTE'
        reserva.save()
        messages.success(request, 'Estado de pago actualizado')
    return HttpResponseRedirect(reverse('listar_reservas'))


@login_required
def eliminar_reserva(request, id):
    if request.session.get('rol') != 'ADMIN':
        messages.error(request, 'No tienes permisos')
        return HttpResponseRedirect(reverse('dashboard'))
    reserva = get_object_or_404(Inscripcion, id=id)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'Reserva eliminada')
    return HttpResponseRedirect(reverse('listar_reservas'))
