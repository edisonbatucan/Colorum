from rest_framework import serializers
from vehicle.models import Vehicle
from django.conf import settings


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'person', 'car_name', 'price', 'num_seats', 'wheel_size', 'car_type')
        model = Vehicle

class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}