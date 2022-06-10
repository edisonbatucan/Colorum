from django.shortcuts import render
from rest_framework import generics
from .serializers import VehicleSerializer
from vehicle.models import Vehicle
# Create your views here.

class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetail(generics.RetrieveDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer