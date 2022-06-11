from django.urls import path
from .views import VehicleList, VehicleDetail

app_name ='vehicle_api'

urlpatterns =[
    path('<int:pk>/', VehicleDetail.as_view(), name='detailcreate'),
    path('', VehicleList.as_view(), name='listcreate'),
]