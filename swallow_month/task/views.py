from django.shortcuts import render

from .models import Task
from .Serializer import  TaskSerializer
from rest_framework import viewsets
from rest_framework import filters 

            

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields =['=userId__userName__userName']