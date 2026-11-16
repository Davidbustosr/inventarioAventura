from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone

from experiencias.models import Categoria, Experiencia, Inscripcion


def inicio(request):
    """Pagina publica: se ve sin iniciar sesion."""
    destacadas = Experiencia.objects.filter(activa=True, categoria__activo=True,
                                            fecha__gte=timezone.now())[:6]
    data = {
        'destacadas': destacadas,
        'categorias': Categoria.objects.filter(activo=True),
    }
    return render(request, 'core/inicio.html', data)


@login_required  # si no hay sesion iniciada, manda al login
def dashboard(request):
    """Panel de control: muestra datos distintos segun el rol guardado en la sesion."""
    rol = request.session.get('rol')
    data = {'rol': rol}

    if rol == 'ADMIN':
        data['total_usuarios'] = User.objects.count()
        data['total_categorias'] = Categoria.objects.count()
        data['total_experiencias'] = Experiencia.objects.count()
        data['total_reservas'] = Inscripcion.objects.count()
        data['pendientes'] = Inscripcion.objects.filter(estado_pago='PENDIENTE').count()
        suma = Inscripcion.objects.filter(estado_pago='CONFIRMADO').aggregate(Sum('experiencia__precio'))
        data['recaudado'] = suma['experiencia__precio__sum'] or 0
        data['ultimas_reservas'] = Inscripcion.objects.all().order_by('-fecha_inscripcion')[:5]

    elif rol == 'GUIA':
        mis_experiencias = Experiencia.objects.filter(creador=request.user)
        data['total_experiencias'] = mis_experiencias.count()
        data['proximas'] = mis_experiencias.filter(fecha__gte=timezone.now()).count()
        data['total_inscritos'] = Inscripcion.objects.filter(experiencia__creador=request.user).count()
        data['mis_experiencias'] = mis_experiencias.order_by('fecha')[:5]

    else:  # TURISTA
        mis_reservas = Inscripcion.objects.filter(usuario=request.user)
        data['total_reservas'] = mis_reservas.count()
        data['confirmadas'] = mis_reservas.filter(estado_pago='CONFIRMADO').count()
        data['pendientes'] = mis_reservas.filter(estado_pago='PENDIENTE').count()
        data['proximas'] = mis_reservas.filter(experiencia__fecha__gte=timezone.now())

    return render(request, 'core/dashboard.html', data)
