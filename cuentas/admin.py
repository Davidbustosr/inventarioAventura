from django.contrib import admin

from cuentas.models import Perfil


class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'rol', 'telefono']
    search_fields = ['usuario__username', 'usuario__first_name', 'usuario__last_name']
    list_filter = ['rol']


admin.site.register(Perfil, PerfilAdmin)
