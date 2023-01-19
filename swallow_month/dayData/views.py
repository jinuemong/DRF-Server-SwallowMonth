from django.shortcuts import render

from .models import DayData,Task
from .Serializer import DayDataSeralizer, TaskSerializer
from rest_framework import viewsets
from rest_framework import filters 

class DayDataViewSet(viewsets.ModelViewSet):
    
    queryset = DayData.objects.all()
    serializer_class = DayDataSeralizer
    filter_backends = [filters.SearchFilter]
    
    def get_queryset(self):
        userName= self.request.query_params.get('userName')
        KeyDate = self.request.query_params.get('KeyDate')
        
        # user + key data 검색 (1개 쿼리 반환)
        if userName and KeyDate:
            queryset =self.queryset.filter(username__username__username  = userName) \
            & self.queryset.filter(KeyDate__username__username  = KeyDate)     
            return queryset
        # user만 검색 (dayData리스트 반환)
        if KeyDate:
            queryset =self.queryset.filter(KeyDate__username__username  = KeyDate)
            return queryset
        # else
        return self.queryset
            
            

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields =['=userId__userName__userName']