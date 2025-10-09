from django.urls import path
from .views import UserRegisterview, UserLoginView, UserLogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('register/', UserRegisterview.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]