from email import message
from django.shortcuts import render
from rest_framework import viewsets, filters, generics, permissions
from .serializers import VehicleSerializer
from vehicle.models import Vehicle
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.

class VehicleUserWritePermission(BasePermission):
    message = "Editing the vehicle details is restricted to the admin only"

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.person == request.user

#Vehicle View/Display
class VehicleList(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = VehicleSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Vehicle, id=item)

    # Define Custom Queryset
    def get_queryset(self):
        return Vehicle.objects.all()

class VehicleDetail(generics.RetrieveAPIView, VehicleUserWritePermission):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        id = self.kwargs.get('pk')
        print(id)
        return Vehicle.objects.filter(id=id)

# Vehicle Search
class VehicleListDetailfilter(generics.ListAPIView):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^car_type', '^car_name']

class VehicleSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^car_type', '^car_name']

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.

# Vehicle Admin

class CreateVehicle(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class AdminVehicleDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class EditVehicle(generics.UpdateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

class DeleteVehicle(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()