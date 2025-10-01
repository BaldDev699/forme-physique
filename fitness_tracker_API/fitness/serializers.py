from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Activity

User = get_user_model()

# Serializer for the custom User model which includes password hashing - it ensures passwords are write-only
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']

    # Override create to handle password hashing
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    # Override update to handle password hashing on updates
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
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