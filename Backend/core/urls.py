from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehicle.urls', namespace='vehicle')),
    path('api/', include('vehicle_api.urls', namespace='vehicle_api')),
]
