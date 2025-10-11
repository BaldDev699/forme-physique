from django.db import models
from django.conf import settings
from datetime import date

# model to track fitness activities
class Activity(models.Model):
    # dictionary of activity choices for better data integrity and consistency
    ACTIVITY_CHOICES = [
        ('running', 'Running'),
        ('walking', 'Walking'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('weightlifting', 'Weightlifting'),
        ('yoga', 'Yoga'),
        ('hiking', 'Hiking'),
        ('other', 'Other'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField(null=True, blank=True)
    distance_km = models.FloatField(null=True, blank=True)
    date = models.DateField()
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
    def __str__(self):
        return f"{self.activity_type} on {self.date} for {self.user.username}"
    
class Goal(models.Model):
    GOAL_TYPES = [
        ('distance', 'Distance (km)'),
        ('duration', 'Duration (minutes)'),
        ('calories', 'Calories Burned'),
    ]

    PERIOD_CHOICES = [
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='goals')
    goal_type = models.CharField(max_length=20, choices=GOAL_TYPES)
    target_value = models.FloatField()
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES)
    start_date = models.DateField(default=date.today)
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s {self.goal_type} goal ({self.period})"
    
    class Meta:
        ordering = ['-start_date']
