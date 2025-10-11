from django.urls import path, include
from .views import ActivityViewSet, GoalViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'goals', GoalViewSet, basename='goal')

urlpatterns = [
    path('', include(router.urls))
]