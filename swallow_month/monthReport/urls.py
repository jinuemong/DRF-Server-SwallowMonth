from django.urls import path, include
from .views import MonthViewSet, RecordViewSet
from rest_framework.routers import DefaultRouter

router_monthData = DefaultRouter()
router_monthData.register("monthDatas",MonthViewSet)
router_monthData.register("recodrdDatas",RecordViewSet)
urlpatterns = [
    path('',include(router_monthData.urls))
]
