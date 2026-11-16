"""Carga los datos de prueba que pide la evaluacion:
1 admin, 2 guias (4 experiencias c/u) y 2 turistas (3 reservas c/u).
Uso:  python manage.py poblar_datos
"""
from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from cuentas.models import Perfil
from experiencias.models import Categoria, Experiencia, Inscripcion

CLAVE = 'Aventura2026'  # misma clave de prueba para todos (ver README)


def crear_usuario(username, nombre, apellido, rol, superusuario=False):
    usuario, creado = User.objects.get_or_create(username=username, defaults={
        'first_name': nombre, 'last_name': apellido, 'email': f'{username}@aventurasdelsur.cl',
        'is_staff': superusuario, 'is_superuser': superusuario})
    usuario.set_password(CLAVE)  # guarda la clave encriptada (hash), nunca en texto plano
    usuario.save()
    Perfil.objects.update_or_create(usuario=usuario, defaults={'rol': rol})
    return usuario


class Command(BaseCommand):
    help = 'Crea usuarios, categorias, experiencias e inscripciones de prueba'

    def handle(self, *args, **options):
        admin = crear_usuario('admin', 'Ana', 'Administradora', 'ADMIN', superusuario=True)
        guia1 = crear_usuario('guia1', 'Camila', 'Rojas', 'GUIA')
        guia2 = crear_usuario('guia2', 'Matías', 'Fuentes', 'GUIA')
        turista1 = crear_usuario('turista1', 'Sofía', 'Pérez', 'TURISTA')
        turista2 = crear_usuario('turista2', 'Benjamín', 'Soto', 'TURISTA')

        cats = {}
        for nombre, desc, activo in [
            ('Trekking', 'Caminatas guiadas por senderos del bosque nativo.', True),
            ('Canopy', 'Recorridos en tirolesa sobre el dosel del bosque.', True),
            ('Kayak', 'Navegación por la laguna y el río.', True),
            ('Arriendo de equipos', 'Bicicletas, carpas y equipo de camping.', True),
            ('Observación de aves', 'Temporada cerrada (ejemplo de categoría inactiva).', False),
        ]:
            cats[nombre], _ = Categoria.objects.update_or_create(
                nombre=nombre, defaults={'descripcion': desc, 'activo': activo})

        hoy = timezone.localtime().replace(minute=0, second=0, microsecond=0)  # hora de Chile
        datos = [
            # (guia, titulo, categoria, precio, cupo, dias desde hoy, hora)
            (guia1, 'Trekking Cerro El Mirador', 'Trekking', 15000, 12, 5, 9),
            (guia1, 'Sendero Cascadas Escondidas', 'Trekking', 18000, 10, 9, 8),
            (guia1, 'Canopy Bosque Nativo', 'Canopy', 25000, 8, 12, 11),
            (guia1, 'Arriendo de bicicletas (día completo)', 'Arriendo de equipos', 12000, 20, 3, 10),
            (guia2, 'Kayak Laguna Verde', 'Kayak', 22000, 6, 7, 10),
            (guia2, 'Kayak nocturno con linternas', 'Kayak', 28000, 6, 14, 20),
            (guia2, 'Canopy Extremo 7 Líneas', 'Canopy', 32000, 10, 10, 15),
            (guia2, 'Arriendo equipo de camping', 'Arriendo de equipos', 20000, 15, 4, 12),
        ]
        exps = []
        for guia, titulo, cat, precio, cupo, dias, hora in datos:
            exp, _ = Experiencia.objects.update_or_create(titulo=titulo, defaults={
                'descripcion': f'{titulo}: experiencia al aire libre guiada por personal del ecoparque.',
                'categoria': cats[cat], 'precio': precio, 'cupo_maximo': cupo,
                'fecha': (hoy + timedelta(days=dias)).replace(hour=hora), 'creador': guia, 'activa': True})
            exps.append(exp)

        for turista, indices in [(turista1, [0, 2, 4]), (turista2, [1, 4, 6])]:
            for n, i in enumerate(indices):
                Inscripcion.objects.update_or_create(usuario=turista, experiencia=exps[i], defaults={
                    'estado_pago': 'CONFIRMADO' if n == 0 else 'PENDIENTE'})

        self.stdout.write(self.style.SUCCESS(
            f'Listo: {User.objects.count()} usuarios, {Categoria.objects.count()} categorias, '
            f'{Experiencia.objects.count()} experiencias, {Inscripcion.objects.count()} inscripciones.'))
