from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import Profile
from user.serializers import ProfileSeralizer
from .models import FriendShip,FUser
from .Serializer import FrendShipSerializer,FUserSerializer
from rest_framework import viewsets
from rest_framework import filters,status
import random

class FriendShipViewSet(viewsets.ModelViewSet):

    queryset  = FriendShip.objects.all()
    serializer_class = FrendShipSerializer
    filter_backends = [filters.SearchFilter]



class FUserViewSet(viewsets.ModelViewSet):

    queryset = FUser.objects.all()
    serializer_class = FUserSerializer
    filter_backends = [filters.SearchFilter]


# 랜덤유저 생성 
# userName을 받음 
class RandomUserView(APIView):

    def post(self,request):
        Profile_list = Profile.objects.all() # 전체 리스트 집합
        # 쿼리셋을 리스트로 변환 (name만 추출 )
        Profile_list = [Profile_list[i].userName for i in range(0,len(Profile_list))] 

        # 내  이름 
        userName = request.data['userName']
        # 내 친구 리스트 받기 
        put_list = FUser.objects.filter(userName = userName)
        # 친구 리스트 이름 추출   
        excludeList = set([put_list[i].otherUser for i in range(0,len(put_list))])
        # 제외 리스트에 나 추가 
        excludeList.add(userName)

        # 나와 친구가 아닌 리스트 얻기 
        profileList = [i for i in Profile_list if i not in excludeList]

        # 리스트가 10이하라면 n명 만큼 추출 
        rand_int = len(profileList) if len(profileList)<=10 else 10
        rand_list = random.sample(profileList,rand_int)

        # 랜덤 리스트를 프로필로 추출 
        randList = [ProfileSeralizer(put).data for put in rand_list]

        return Response(randList,status=status.HTTP_200_OK)