from django.urls import path, include
from .views import TaskViewSet,DayDataViewSet
from rest_framework.routers import DefaultRouter

router_daydata = DefaultRouter()
router_daydata.register('dayDatas',DayDataViewSet)
router_daydata.register("tasks",TaskViewSet)

urlpatterns = [
    path('',include(router_daydata.urls))
]
