from .views import FUserViewSet,FriendShipViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RandomUserView,MyFriendList
router_routine = DefaultRouter()
router_routine.register('friendShips',FriendShipViewSet)
router_routine.register('fusers',FUserViewSet)


urlpatterns = [
    path('myFrineds/',MyFriendList.as_view()),
    path('randomProfile/',RandomUserView.as_view()),
    path('',include(router_routine.urls)),
]
