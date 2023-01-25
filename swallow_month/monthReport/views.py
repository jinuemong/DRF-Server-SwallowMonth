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
        keyDate = self.request.query_params.get('keyDate')
        print("sadaasdasd1",userName,keyDate)
        # user + key data 검색 (1개 쿼리 반환)
        if userName and keyDate:
            print("sadaasdasd2",userName,keyDate)
            queryset =self.queryset.filter(userId__userName  = userName) \
            & self.queryset.filter(keyDate = keyDate)     
            return queryset
        # user만 검색 (dayData리스트 반환)
        elif keyDate:
            queryset =self.queryset.filter(keyDate  = keyDate)
            return queryset
        # else
        return self.queryset