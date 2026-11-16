from django.contrib import admin

from experiencias.models import Categoria, Experiencia, Inscripcion


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'activo']
    search_fields = ['nombre']
    list_filter = ['activo']


class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'categoria', 'precio', 'cupo_maximo', 'fecha', 'creador', 'activa']
    search_fields = ['titulo', 'descripcion']
    list_filter = ['categoria', 'activa', 'creador']


class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'experiencia', 'fecha_inscripcion', 'estado_pago']
    search_fields = ['usuario__username', 'experiencia__titulo']
    list_filter = ['estado_pago', 'experiencia__categoria']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Experiencia, ExperienciaAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)
