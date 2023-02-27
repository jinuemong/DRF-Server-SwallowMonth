from django.shortcuts import render


from .models import FriendShip,FUser
from .Serializer import FrendShipSerializer,FUserSerializer
from rest_framework import viewsets
from rest_framework import filters

class FriendShipViewSet(viewsets.ModelViewSet):

    queryset  = FriendShip.objects.all()
    serializer_class = FrendShipSerializer
    filter_backends = [filters.SearchFilter]



class FUserViewSet(viewsets.ModelViewSet):

    queryset = FUser.objects.all()
    serializer_class = FUserSerializer
    filter_backends = [filters.SearchFilter]