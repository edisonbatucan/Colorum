from django.urls import path
from .views import pickup_list

urlpatterns = [
    path('pickups/', pickup_list),
]