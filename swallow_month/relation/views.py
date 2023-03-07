from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import Profile
from user.serializers import ProfileSeralizer
from .models import FriendShip,FUser, Alarm , Message
from .Serializer import FrendShipSerializer,FUserSerializer,AlarmSerializer, MessageSerializer
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

class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all().order_by('createTime')
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=frId__frId']

class AlarmViewSet(viewsets.ModelViewSet):
    
    queryset = Alarm.objects.all().order_by('createTime')
    serializer_class = AlarmSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=userId__userName__userName']

    

# 친구 리스트 (프로필 )
class FriendListView(APIView):

    def post(self,request):
        try:
            userName = request.data['userName']
            friendList = FUser.objects.filter(userId = userName)
            # 두 데이터 받기 
            friendList = [ProfileSeralizer(Profile.objects.get(profileId=put.otherUser)).data 
                          for put in friendList]
            return Response(friendList,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

# 랜덤유저 생성 
# userName을 받음 
class RandomUserView(APIView):

    def post(self,request):
        Profile_list = Profile.objects.all() # 전체 리스트 집합
        # 쿼리셋을 리스트로 변환 (profileId 추출 )
        Profile_list = [Profile_list[i].profileId for i in range(0,len(Profile_list))] 

        # 내  이름 
        pId = request.data['profileId']
        myProfile = Profile.objects.get(profileId = pId)
        # 내 친구 리스트 받기 
        put_list = FUser.objects.filter(userId = myProfile.userName)
        
        # 친구 리스트 profileId 추출   
        excludeList = set([put_list[i].otherUser for i in range(0,len(put_list))])
        # 제외 리스트에 나 추가 
        excludeList.add(int(pId))

        # 나와 친구가 아닌 리스트 얻기 
        profileList = [i for i in Profile_list if i not in excludeList]

        # 리스트가 10이하라면 n명 만큼 추출 
        rand_int = len(profileList) if len(profileList)<=10 else 10
        rand_list = random.sample(profileList,rand_int)

        # 랜덤 리스트를 프로필로 추출  
        randList = [ProfileSeralizer(Profile.objects.get(profileId=put))
                    .data for put in rand_list]

        return Response(randList,status=status.HTTP_200_OK)



# # 친구 리스트 (채팅방)
class MessageListView(APIView):

    def post(self,request):
        try:
            userName = request.data['userName']
            friendList = FUser.objects.filter(userName = userName)
            # 두 데이터 받기 
            friendList = [[FrendShipSerializer(put.frId).data
                           ,ProfileSeralizer(put.otherUser).data] 
                          for put in friendList]
            return Response(friendList,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

## is frined? username ,targetUser (profile Id) 받음 
# 두 관계를 확인
class CheckFriendView(APIView):

    def post(self,request):

        try:
            userName = request.data['userName']
            targetUser = request.data['targetUser'] #profileId
            
            fuser = FUser.objects.filter(userId=userName) \
            & FUser.objects.filter(otherUser=targetUser)

            if fuser.exists():
                fuser = FUserSerializer(fuser[0]).data
                friendData = FrendShipSerializer(FriendShip.objects.get(frId=fuser["frId"])).data
                profile=ProfileSeralizer(Profile.objects.get(profileId=fuser["otherUser"])).data 
                
                return Response({"friendData":friendData,"profile":profile},status=status.HTTP_200_OK)
                          
            else:
                print("!@#!@#!@#test 2 ","no dat ")
                return Response([],status=status.HTTP_200_OK)


        except:
            print("!@#!@#!@#test 3 ","no dat ")
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

            # if fuser.exists(): # 단순 요청 관계
            #     # user change
            #     user1 = Profile.objects.get(profileId = targetUser).userName
            #     user2 = Profile.objects.get(userName = userName).profileId
            #     fuser2 = FUser.objects.filter(userName=user1,otherUser=user2)
                
            #     if fuser2.exists(): #완전 친구 관계
            #         friendList = [FrendShipSerializer(fuser2.frId).data
            #                       ,ProfileSeralizer(fuser2.otherUser).data] 
            #         return Response(friendList,status=status.HTTP_200_OK)
                
            #     else: # 단순 요청 관계
            #         friendList = [FrendShipSerializer(fuser.frId).data
            #                       ,ProfileSeralizer(fuser.otherUser).data] 
            #         return Response(friendList,status=status.HTTP_200_OK)
                          