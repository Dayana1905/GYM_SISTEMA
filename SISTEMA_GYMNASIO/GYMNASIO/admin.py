from django.contrib import admin
from .models import Cliente, Plan, Inscripcion

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'email', 'telefono')  
    search_fields = ('cedula', 'nombre', 'email')  
    list_filter = ('cedula',)

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre_plan', 'precio', 'duracion_meses')  
    search_fields = ('nombre_plan',) 
@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'plan', 'fecha_inicio', 'fecha_fin')  
    search_fields = ('cedula__cedula', 'plan__nombre_plan')  
 