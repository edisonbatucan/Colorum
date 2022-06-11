from email import message
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from .serializers import VehicleSerializer
from vehicle.models import Vehicle
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.

class VehicleUserWritePermission(BasePermission):
    message = "Editing the vehicle details is restricted to the admin only"

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.person == request.user

class VehicleList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = VehicleSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Vehicle, id=item)

    # Define Custom Queryset
    def get_queryset(self):
        return Vehicle.objects.all()

# class VehicleList(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly] 
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer

# class VehicleDetail(viewsets.ModelViewSet, VehicleUserWritePermission):
#     permission_classes = [VehicleUserWritePermission]
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer