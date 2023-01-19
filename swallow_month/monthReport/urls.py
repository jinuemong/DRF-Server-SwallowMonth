from django.urls import path, include
from .views import MonthViewSet
from rest_framework.routers import DefaultRouter

router_monthData = DefaultRouter()
router_monthData.register("monthDatas",MonthViewSet)

urlpatterns = [
    path('',include(router_monthData.urls))
]
