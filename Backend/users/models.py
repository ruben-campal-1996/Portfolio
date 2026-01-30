from django.db import models
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
    return f'user_{instance.id}/documents/{filename}'

class User(AbstractUser):
    # Definición de Roles
    class Role(models.TextChoices):
        DIRECTOR = 'DIRECTOR', 'Director'
        GERENTE = 'GERENTE', 'Gerente de Proyectos'
        TRABAJADOR = 'TRABAJADOR', 'Trabajador'
        INVITADO = 'INVITADO', 'Invitado'

    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    
    # Campo de Rol
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.INVITADO,
        verbose_name="Rol"
    )
    
    documentation = models.FileField(
        upload_to=user_directory_path, 
        blank=True, 
        null=True, 
        verbose_name="Documentación"
    )

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"