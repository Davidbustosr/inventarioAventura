from django.urls import path

from experiencias import views

urlpatterns = [
    # CRUD Categorias (Administrador)
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/nueva/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),

    # Gestion de Experiencias (Administrador y Guia)
    path('gestion/', views.listar_experiencias, name='listar_experiencias'),
    path('gestion/nueva/', views.crear_experiencia, name='crear_experiencia'),
    path('gestion/editar/<int:id>/', views.editar_experiencia, name='editar_experiencia'),
    path('gestion/eliminar/<int:id>/', views.eliminar_experiencia, name='eliminar_experiencia'),
    path('gestion/inscritos/<int:id>/', views.inscritos_experiencia, name='inscritos_experiencia'),

    # Catalogo y reservas (Turista)
    path('catalogo/', views.catalogo, name='catalogo'),
    path('detalle/<int:id>/', views.detalle_experiencia, name='detalle_experiencia'),
    path('reservar/<int:id>/', views.reservar, name='reservar'),
    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('mis-reservas/pagar/<int:id>/', views.pagar_reserva, name='pagar_reserva'),
    path('mis-reservas/cancelar/<int:id>/', views.cancelar_reserva, name='cancelar_reserva'),

    # Todas las reservas (Administrador)
    path('reservas/', views.listar_reservas, name='listar_reservas'),
    path('reservas/estado/<int:id>/', views.cambiar_estado_reserva, name='cambiar_estado_reserva'),
    path('reservas/eliminar/<int:id>/', views.eliminar_reserva, name='eliminar_reserva'),
]
