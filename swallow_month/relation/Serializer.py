from .models import FriendShip,FUser
from user.models import Profile
from rest_framework import serializers


class FUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        managed = True
        model = FUser
        db_table = "FUsers"
        fields = "__all__"

class FrendShipSerializer(serializers.ModelSerializer):

    fUserPost = FUserSerializer(many = True,read_only = True)
    class Meta:
        managed = True
        model = FriendShip
        db_table = "FriendShips"
        fields = ["frId","name","fUserPost"]