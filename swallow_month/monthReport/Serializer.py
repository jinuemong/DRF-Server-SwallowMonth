from .models import MonthData
from rest_framework import serializers
from task.Serializer import TaskSerializer

class MonthDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        managed = True
        model = MonthData
        db_table = "MonthDatas"
        fields = ['monthId','userId','keyDate','totalPer','totalPoint',
                  'doneTask','clearRoutine']