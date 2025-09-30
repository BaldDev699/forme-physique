from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Serializer for the custom User model which includes password hashing - it ensures passwords are write-only
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user