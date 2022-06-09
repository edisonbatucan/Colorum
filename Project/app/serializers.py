import imp
from rest_framework import serializers
from .models import SUV, PickUp


class SUVSerializer(serializers.Serializer):
    car_name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    num_seats = serializers.IntegerField()
    wheel_size = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return SUV.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.car_name = validated_data.get('car_name', instance.car_name)
        instance.price = validated_data.get('price', instance.price)
        instance.num_seats = validated_data.get(
            'num_seats', instance.num_seats)
        instance.wheel_size = validated_data.get(
            'wheel_size', instance.wheel_size)
        instance.save()
        return instance

class PickUpSerializer(serializers.Serializer):
    car_name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    num_seats = serializers.IntegerField()
    wheel_size = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return SUV.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.car_name = validated_data.get('car_name', instance.car_name)
        instance.price = validated_data.get('price', instance.price)
        instance.num_seats = validated_data.get(
            'num_seats', instance.num_seats)
        instance.wheel_size = validated_data.get(
            'wheel_size', instance.wheel_size)
        instance.save()
        return instance
