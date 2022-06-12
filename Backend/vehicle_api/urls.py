from .views import DeleteVehicle, EditVehicle, VehicleList, VehicleListDetailfilter, VehicleDetail, CreateVehicle, AdminVehicleDetail
from rest_framework.routers import DefaultRouter
from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


app_name ='vehicle_api'

# router = DefaultRouter()
# router.register('', VehicleList, basename='vehicle')
# router.register('', VehicleListDetailfilter, basename='search')
# urlpatterns = router.urls


urlpatterns =[
    path('<int:pk>/', VehicleDetail.as_view(), name='detailcreate'),
    path('search/', VehicleListDetailfilter.as_view(), name='vehiclesearch'),
    path('', VehicleList.as_view(), name='listcreate'),
    # Vehicle Admin URLs
    path('admin/create/', CreateVehicle.as_view(), name='createvehicle'),
    path('admin/edit/vehicledetail/<int:pk>/', AdminVehicleDetail.as_view(), name='admindetailvehicle'),
    path('admin/edit/<int:pk>/', EditVehicle.as_view(), name='editvehicle'),
    path('admin/delete/<int:pk>/', DeleteVehicle.as_view(), name='deletevehicle'),
]