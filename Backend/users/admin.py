from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Esto añade tus campos al formulario de edición del Admin
    fieldsets = UserAdmin.fieldsets + (
        ('Información Extra', {'fields': ('role', 'phone', 'documentation')}),
    )
    # Esto añade las columnas en la lista de usuarios
    list_display = ['username', 'email', 'role', 'is_staff']
    list_filter = ['role', 'is_staff']

admin.site.register(User, CustomUserAdmin)