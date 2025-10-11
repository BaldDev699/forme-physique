from django.db import models
from django.conf import settings
from fitness.models import Goal

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('info', 'Information'),
        ('warning', 'Warning'),
        ('error', 'Error'),
        ('success', 'Success'),
        ('alert', 'Alert'),
        ('reminder', 'Reminder'),
        ('goal achievement', 'Goal Achievement'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES, default='info')

    def __str__(self):
        return f"{self.notification_type} for {self.user.username}"
