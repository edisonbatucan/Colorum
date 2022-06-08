import imp
from attr import field
from rest_framework import serializers
from .models import SUV


class SUVSerializer(serializers.ModelSerializer):
    class Meta:
        model = SUV
        # fields = ['id', 'car_name', 'price', 'num_seats', 'wheel_size']
        fields = '__all__'
