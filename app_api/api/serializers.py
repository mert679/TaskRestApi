from django.contrib.auth.models import User
from rest_framework import serializers
from app_api.models import Car

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['model']
