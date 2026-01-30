from django.contrib import admin
from .models import Task
# No necesitamos importar User si solo usamos los nombres de los campos en list_filter

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Columnas que verás en la tabla de resumen
    list_display = ('title', 'status', 'created_by', 'assigned_to', 'created_at')
    
    # Filtros laterales (Quitamos la línea 9 que fallaba)
    list_filter = ('status', 'created_by', 'assigned_to')
    
    # Buscador por texto
    search_fields = ('title', 'description')
    
    # Esto hará que los desplegables de usuario sean más rápidos si tienes muchos
    raw_id_fields = ('created_by', 'assigned_to')