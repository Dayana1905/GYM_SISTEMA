from rest_framework import serializers
from .models import Cliente, Plan, Inscripcion


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' 


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__' 


class InscripcionSerializer(serializers.ModelSerializer):
    cliente = ClientesSerializer() 
    plan = PlanSerializer()        

    class Meta:
        model = Inscripcion
        fields = '__all__'  