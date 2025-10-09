from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets, filters
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Count
from django.db.models.functions import TruncWeek, TruncMonth
from .models import Activity
from django.contrib.auth import get_user_model
from .serializers import ActivitySerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

        
# Activity ViewSet to handle CRUD operations and analytics
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['activity_type', 'date']
    ordering_fields = ['date', 'duration_minutes', 'calories_burned']
    search_fields = ['notes']

    def get_queryset(self):
        # Limit activities to those owned by the authenticated user
        user = self.request.user
        if not user.is_authenticated:
            return Activity.objects.none()
        qs = Activity.objects.filter(user=user)
        start = self.request.query_params.get('start_date')
        end = self.request.query_params.get('end_date')
        if start and end:
            qs = qs.filter(date__range=[start, end])
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='metrics')
    def metrics(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        start = request.query_params.get('start')
        end = request.query_params.get('end')
        group = request.query_params.get('group')  # weekly or monthly trend grouping

        qs = Activity.objects.filter(user=user)
        if start:
            qs = qs.filter(date__gte=start)
        if end:
            qs = qs.filter(date__lte=end)

        totals = qs.aggregate(
            total_duration=Sum('duration_minutes'),
            total_distance=Sum('distance_km'),
            total_calories=Sum('calories_burned'),
            count=Count('id')
        )

        response = {
            'total_duration_min': totals['total_duration'] or 0,
            'total_distance': float(totals['total_distance'] or 0),
            'total_calories': totals['total_calories'] or 0,
            'activity_count': totals['count'] or 0,
        }

        # optional trends
        if group == 'week':
            trend = qs.annotate(period=TruncWeek('date')) \
                      .values('period') \
                      .annotate(total_duration=Sum('duration_minutes'), total_distance=Sum('distance_km'), total_calories=Sum('calories_burned')) \
                      .order_by('period')
            response['trend'] = list(trend)
        elif group == 'month':
            trend = qs.annotate(period=TruncMonth('date')) \
                      .values('period') \
                      .annotate(total_duration=Sum('duration_minutes'), total_distance=Sum('distance_km'), total_calories=Sum('calories_burned')) \
                      .order_by('period')
            response['trend'] = list(trend)

        return Response(response)