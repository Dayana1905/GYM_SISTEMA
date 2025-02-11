from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Plan, Inscripcion
from .serializers import ClientesSerializer, PlanSerializer, InscripcionSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
