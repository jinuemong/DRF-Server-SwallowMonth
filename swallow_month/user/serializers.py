from .models import User
from rest_framework import serializers
from django.utils import timezone


#serializer를 통해 사용자 등록을 위한 
# 요청(request)과 응답(response)을 직렬화(serialize)

# 등록 , 로그인, 유저 정보 serializer 생성
