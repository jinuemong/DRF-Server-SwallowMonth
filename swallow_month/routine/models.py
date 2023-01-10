from django.db import models


class Routine(models.Model):
    routineId = models.BigAutoField(primary_key=True,help_text="Routine ID")
    keyDate = models.CharField(max_length=20,default=False)
    text = models.TextField()
    cycle = models.IntegerField()
    startNum = models.IntegerField()
    totalRoutine = models.IntegerField()
    clearRoutine = models.IntegerField()
    iconType = models.IntegerField(default=0)
    topText = models.CharField(max_length=30,default=False)


class DayRoutine(models.Model):
    id = models.BigAutoField(primary_key=True,help_text="DayRoutine ID")
    routineId = models.ForeignKey(Routine,on_delete=models.CASCADE
                                  ,related_name="dayRoutinePost",db_column='routineId',to_field='routineId')
    dayIndex =  models.IntegerField()
    clear = models.BooleanField(default=False)