from django.db import models
from user.models import User
# Create your models here.

class MonthData(models.Model):
    monthId = models.BigAutoField(primary_key=True,help_text="month ID")
    userId = models.ForeignKey(User,on_delete=models.CASCADE
                               ,related_name='monthPost',to_field='userName')
    keyDate = models.CharField(max_length=20,default=False)
    totalPer = models.IntegerField()
    totalPoint = models.IntegerField()
    doneTask = models.IntegerField()
    clearRoutine = models.IntegerField()