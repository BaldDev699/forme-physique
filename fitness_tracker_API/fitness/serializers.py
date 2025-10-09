from rest_framework import serializers
from .models import Activity
    
# Serializer for the Activity model to handle fitness activity data
class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Activity
        fields = [
            'id', 'user', 'activity_type', 'duration_minutes', 'calories_burned',
            'distance_km', 'date', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        if 'activity_type' not in data:
            raise serializers.ValidationError("Activity type is required.")
        if 'duration_minutes' not in data or data.get('duration_minutes') is None:
            raise serializers.ValidationError("Duration is required.")
        if data['duration_minutes'] <= 0:
            raise serializers.ValidationError("Duration must be a positive integer.")
        if 'calories_burned' in data and data['calories_burned'] is not None and data['calories_burned'] < 0:
            raise serializers.ValidationError("Calories burned cannot be negative.")
        if 'distance_km' in data and data['distance_km'] is not None and data['distance_km'] < 0:
            raise serializers.ValidationError("Distance cannot be negative.")
        if 'date' not in data or data.get('date') is None:
            raise serializers.ValidationError("Date is required.")
        return data