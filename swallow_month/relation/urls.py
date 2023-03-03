from .views import FUserViewSet,FriendShipViewSet,AlarmViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RandomUserView,MyFriendList
router_routine = DefaultRouter()
router_routine.register('friendShips',FriendShipViewSet)
router_routine.register('fusers',FUserViewSet)
router_routine.register('alarms',AlarmViewSet)

urlpatterns = [
    path('myFriends/',MyFriendList.as_view()),
    path('randomProfile/',RandomUserView.as_view()),
    path('',include(router_routine.urls)),
]
