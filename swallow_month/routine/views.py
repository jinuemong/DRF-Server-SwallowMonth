from django.shortcuts import render

from .models import Routine,DayRoutine
from .Serializer import RoutineSerializer,DayRoutineSerializer
from rest_framework import viewsets
from rest_framework import filters

class RoutineViewSet(viewsets.ModelViewSet):
    
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    filter_backends = [filters.SearchFilter]
    search_fields =['=userId__userName__userName']

class DayRoutineViewSet(viewsets.ModelViewSet):
    
    queryset = DayRoutine.objects.all()
    serializer_class = DayRoutineSerializer
    filter_backends = [filters.SearchFilter]
    search_fields =['=userId__userName__userName']
