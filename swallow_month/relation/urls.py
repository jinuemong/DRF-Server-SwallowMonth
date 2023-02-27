from .views import FUserViewSet,FriendShipViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router_routine = DefaultRouter()
router_routine.register('friendShips',FriendShipViewSet)
router_routine.register('fusers',FUserViewSet)


urlpatterns = [
     path('',include(router_routine.urls))
]
