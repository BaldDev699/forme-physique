from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet

urlpatterns = [
    path('activities/', ActivityViewSet.as_view({'get': 'list', 'post': 'create'}), name='activity-list'),
    path('activities/<int:pk>/', ActivityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='activity-detail'),
]