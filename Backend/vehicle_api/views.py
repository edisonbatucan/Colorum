<<<<<<< HEAD
from email import message
=======
>>>>>>> cfeec00b6b0276e891dcaa192fa7c22a56a03dfb
from django.shortcuts import render
from rest_framework import generics
from .serializers import VehicleSerializer
from vehicle.models import Vehicle
<<<<<<< HEAD
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
=======
# Create your views here.

class VehicleList(generics.ListCreateAPIView):
>>>>>>> cfeec00b6b0276e891dcaa192fa7c22a56a03dfb
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


<<<<<<< HEAD
class VehicleDetail(generics.RetrieveUpdateDestroyAPIView, VehicleUserWritePermission):
    permission_classes = [VehicleUserWritePermission]
=======
class VehicleDetail(generics.RetrieveDestroyAPIView):
>>>>>>> cfeec00b6b0276e891dcaa192fa7c22a56a03dfb
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer