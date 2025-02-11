from django.db import models
from django.core.validators import MinLengthValidator
from .validadores import validacion_numeros

# Create your models here.
class Cliente(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True, validators=[MinLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'  
        db_table = 'Cliente'
        
    def __str__(self):
        return f"{self.nombre} {self.apellido}"  

class Plan(models.Model):
    codigo = models.AutoField(primary_key=True) 
    nombre_plan = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    duracion_meses = models.IntegerField()

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'
        db_table = 'Plan'

    def __str__(self):
        return self.nombre_plan  

class Inscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        verbose_name = 'Inscripción'
        verbose_name_plural = 'Inscripciones'
        db_table = 'Inscripcion'

    def __str__(self):
        
        return f"{self.cedula.nombre} {self.cedula.apellido} - {self.plan.nombre_plan}"
