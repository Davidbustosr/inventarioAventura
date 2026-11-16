from django.urls import path

from cuentas import views

urlpatterns = [
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.mi_perfil, name='mi_perfil'),
    # CRUD de usuarios (Administrador)
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
]
