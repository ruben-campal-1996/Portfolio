from django.db import models
from django.conf import settings

class Task(models.Model):
    class Status(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        EJECUCION = 'EJECUCION', 'En ejecución'
        FINALIZADA = 'FINALIZADA', 'Finalizada'
        CANCELADA = 'CANCELADA', 'Cancelada'

    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDIENTE,
        verbose_name="Estado"
    )
    
    # Usuario que CREA la tarea (quien la manda)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='created_tasks',
        verbose_name="Creado por"
    )

    # Usuario ASIGNADO a la tarea (quien la hace)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, # Si el usuario se borra, la tarea queda sin asignar pero no se borra
        null=True,
        blank=True,
        related_name='assigned_tasks',
        verbose_name="Asignado a"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title