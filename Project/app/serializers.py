import email
import imp

#from grpc import services
#from attr import field
from rest_framework import serializers
from .models import SUV, PickUp
from django.contrib.auth.models import User


class SUVSerializer(serializers.ModelSerializer):
    class Meta:
        model = SUV
        # fields = ['id', 'car_name', 'price', 'num_seats', 'wheel_size']
        fields = '__all__'

class PickUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickUp
        #fields = ['id', 'car_name', 'price', 'num_seats', 'wheel_size']
        fields = '__all__'

class RegristrationSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length =60, min_length =5)
    email = serializers.CharField(max_length =60, min_length =5)
    password = serializers.CharField(max_length=150, write_only=True)
    class Meta:
        model = User
        fields = ('username','email','password')

    def validate(self, args):
        email = args.get('email',None)
        username = args.get('username',None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('Username already exists')})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
