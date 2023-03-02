from user.models import User
from django.db import models
# two member
class FriendShip(models.Model):
    frId = models.BigAutoField(primary_key=True,help_text="Friendship ID")
    name = models.CharField(max_length=30,default=False)

class FUser(models.Model):
    fuId = models.BigAutoField(primary_key=True,help_text="FUser ID")
    frId = models.ForeignKey(FriendShip,on_delete=models.CASCADE
                             ,related_name="fUserPost",to_field="frId")
    userId = models.ForeignKey(User,on_delete=models.CASCADE
                               ,related_name="fUserPost",to_field="userName")
    otherUser = models.IntegerField(default=False)

class Alarm(models.Model):
    alarmId = models.BigAutoField(primary_key=True,help_text="Alarm ID")
    userId = models.ForeignKey(User,on_delete=models.CASCADE
                               ,related_name="AlarmPost",to_field="userName")
    type = models.CharField(default=False)