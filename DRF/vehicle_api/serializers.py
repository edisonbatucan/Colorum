from rest_framework import serializers
from vehicle.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'car_name', 'price', 'num_seats', 'wheel_size','author', 'car_type')
        model = Post