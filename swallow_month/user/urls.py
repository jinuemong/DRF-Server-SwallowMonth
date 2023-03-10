from django.urls import path,include
from .views import RegistrationAPIView, LoginAPIView,UpdateProfileView
from .views import UserRetrieveUpdateAPIView,ProfileViewSet
from rest_framework.routers import DefaultRouter

router_user = DefaultRouter()
router_user.register('profile',ProfileViewSet)

urlpatterns = [
    path('register/',RegistrationAPIView.as_view()),
    path('login/',LoginAPIView.as_view()),
    path('current/',UserRetrieveUpdateAPIView.as_view()),
    path('',include(router_user.urls)),
    path('update/profile/',UpdateProfileView.as_view()),

]
