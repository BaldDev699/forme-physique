from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# user model which extends AbstractUser
class User(AbstractUser):
    pass

# model to track fitness activities
class Activity(models.Model):
    # dictionary of activity choices for better data integrity
    ACTIVITY_CHOICES = [
        ('running', 'Running'),
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
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
    def __str__(self):
        return f"{self.activity_type} on {self.date} for {self.user.username}"
