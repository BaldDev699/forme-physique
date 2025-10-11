from django.urls import path, include
from .views import ActivityViewSet, GoalViewSet

urlpatterns = [
    path('activities/', ActivityViewSet.as_view({'get': 'list', 'post': 'create'}), name='activity-list'),
    path('activities/<int:pk>/', ActivityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='activity-detail'),
    path('goals/', GoalViewSet.as_view({'get': 'list', 'post': 'create'}), name='goal-list'),
    path('goals/<int:pk>/', GoalViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='goal-detail'),
]