"""
Rutas principales del proyecto inventarioAventura.
Cada app tiene su propio urls.py y aqui solo se incluyen (include).
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),                    # Django Admin
    path('', include('core.urls')),                     # Landing y panel de control
    path('cuentas/', include('cuentas.urls')),          # Login, registro, usuarios
    path('experiencias/', include('experiencias.urls')),  # Categorias, experiencias, reservas
]
