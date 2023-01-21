from django.shortcuts import render

from .models import Routine,DayRoutine
from .Serializer import RoutineSerializer,DayRoutineSerializer
from rest_framework import viewsets
from rest_framework import filters

class RoutineViewSet(viewsets.ModelViewSet):
    
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    filter_backends = [filters.SearchFilter]
    def get_queryset(self):
        userName= self.request.query_params.get('userName')
        KeyDate = self.request.query_params.get('KeyDate')
        # user + key data 검색 >  이번달 리스트 뽑기 
        if userName and KeyDate:
            queryset =self.queryset.filter(username__username__username  = userName) \
            & self.queryset.filter(KeyDate  = KeyDate)     
            return queryset
        # else
        return self.queryset
    
class DayRoutineViewSet(viewsets.ModelViewSet):
    
    queryset = DayRoutine.objects.all()
    serializer_class = DayRoutineSerializer
    filter_backends = [filters.SearchFilter]
