from email import message
from django.shortcuts import render
from rest_framework import generics
from .serializers import VehicleSerializer
from vehicle.models import Vehicle
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly
# Create your views here.

class VehicleUserWritePermission(BasePermission):
    message = "Editing the vehicle details is restricted to the admin only"

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.person == request.user



class VehicleList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView, VehicleUserWritePermission):
    permission_classes = [VehicleUserWritePermission]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer