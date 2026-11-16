from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)  # estado: activo / inactivo

    def __str__(self):
        return self.nombre


class Experiencia(models.Model):
    """El 'producto' del ecoparque: trekking, canopy, kayak, arriendo de equipos..."""

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()        # precio en pesos chilenos
    cupo_maximo = models.PositiveIntegerField()
    fecha = models.DateTimeField()                # fecha y hora de realizacion
    activa = models.BooleanField(default=True)    # el turista solo ve las activas
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='experiencias')
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiencias_creadas')

    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return self.titulo

    def inscritos(self):
        return self.inscripciones.count()

    def cupos_disponibles(self):
        return self.cupo_maximo - self.inscritos()


class Inscripcion(models.Model):
    """Tabla intermedia: que turista (User) va a que experiencia."""

    PENDIENTE = 'PENDIENTE'
    CONFIRMADO = 'CONFIRMADO'
    ESTADOS_PAGO = [
        (PENDIENTE, 'Pendiente'),
        (CONFIRMADO, 'Confirmado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inscripciones')
    experiencia = models.ForeignKey(Experiencia, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado_pago = models.CharField(max_length=10, choices=ESTADOS_PAGO, default=PENDIENTE)

    class Meta:
        verbose_name_plural = 'Inscripciones'
        # Un turista no puede inscribirse dos veces en la misma experiencia
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'experiencia'], name='inscripcion_unica'),
        ]

    def __str__(self):
        return f"{self.usuario.username} -> {self.experiencia.titulo}"
