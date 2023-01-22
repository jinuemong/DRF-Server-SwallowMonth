from django.shortcuts import render

from .models import Task
from .Serializer import  TaskSerializer
from rest_framework import viewsets
from rest_framework import filters 

            

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    
    def get_queryset(self):
        userName= self.request.query_params.get('userName')
        KeyDate = self.request.query_params.get('KeyDate')
        dayIndex = self.request.query_params.get('dayIndex')
        # user + key data 검색 >  이번달 리스트 뽑기 
        if userName and KeyDate:
            queryset =self.queryset.filter(userId__userName  = userName) \
            & self.queryset.filter(KeyDate  = KeyDate)     
            return queryset
        # user + key date + day 검색 > 하루 리스트 뽑기
        if userName and KeyDate and dayIndex:
            queryset =self.queryset.filter(userId__userName  = userName) \
            & self.queryset.filter(KeyDate  = KeyDate) & self.queryset.filter(dayIndex=dayIndex)
            return queryset
        # else
        return self.queryset