from django.shortcuts import render
from .models import MonthData
from .Serializer import MonthDataSerializer
from rest_framework import viewsets
from rest_framework import filters


class MonthViewSet(viewsets.ModelViewSet):
    
    queryset = MonthData.objects.all()
    serializer_class = MonthDataSerializer
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        userName= self.request.query_params.get('userName')
        KeyDate = self.request.query_params.get('KeyDate')
        
        # user + key data 검색 (1개 쿼리 반환)
        if userName and KeyDate:
            queryset =self.queryset.filter(username__username__username  = userName) \
            & self.queryset.filter(KeyDate  = KeyDate)     
            return queryset
        # user만 검색 (dayData리스트 반환)
        if KeyDate:
            queryset =self.queryset.filter(KeyDate  = KeyDate)
            return queryset
        # else
        return self.queryset