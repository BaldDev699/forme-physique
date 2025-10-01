from django.urls import path, include
from .views import UserRegisterview, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', UserRegisterview.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]