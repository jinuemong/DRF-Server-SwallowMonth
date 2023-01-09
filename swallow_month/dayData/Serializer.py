from .models import DayData,Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        managed = True
        model = Task
        db_table = "Tasks"
        fields = "__all__"

class DayDataSeralizer(serializers.ModelSerializer):
   
   taskPost = TaskSerializer(many = True,read_only=True)
   
   class Meta:
       managed=True
       model = DayData
       db_table = "DayDatas"
       fields = ['dayDataId', 'KeyDate', 'day', 'isSelected',
                 'monthIndex', 'taskPost'] 