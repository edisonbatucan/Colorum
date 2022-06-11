from rest_framework import serializers
from vehicle.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'person', 'car_name', 'price', 'num_seats', 'wheel_size', 'car_type')
        model = Vehicle