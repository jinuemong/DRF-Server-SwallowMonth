from django.shortcuts import render

from .models import DayData,Task
from .Serializer import DayDataSeralizer, TaskSerializer
from rest_framework import viewsets
from rest_framework import filters 

class DayDataViewSet(viewsets.ModelViewSet):
    
    queryset = DayData.objects.all()
    serializer_class = DayDataSeralizer
    filter_backends = [filters.SearchFilter]
    # search_fields =[]

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    # search_fields =[]