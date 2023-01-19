from django.db import models
from user.models import User

class DayData(models.Model):
    dayDataId = models.BigAutoField(primary_key=True,help_text="DayDate ID")
    userId = models.ForeignKey(User,on_delete=models.CASCADE
                               ,related_name='dayDataPost',to_field='userName')
    KeyDate = models.CharField(max_length=20,default=False)
    day = models.IntegerField()
    isSelected = models.BooleanField(default=False)
    monthIndex = models.IntegerField(default=0)

class Task(models.Model):
    id = models.BigAutoField(primary_key=True,help_text="Task ID")
    dayDataId = models.ForeignKey(DayData,on_delete=models.CASCADE
                                  ,related_name="taskPost",db_column='dayDataId',to_field='dayDataId')
    userId = models.ForeignKey(User,on_delete=models.CASCADE
                               ,related_name='taskPost',to_field='userName')
    text = models.TextField()
    isDone = models.BooleanField(default=False)
    iconType = models.IntegerField(default=0)
    level = models.IntegerField()
    per = models.IntegerField(default=0)
