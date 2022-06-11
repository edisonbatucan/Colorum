from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehicle.urls', namespace='vehicle')),
    #endpoint into vehicle api that show all data
    path('api/', include('vehicle_api.urls', namespace='vehicle_api')),
    #user endpoint utilized to register a user
    path('api/user/', include('users.urls', namespace='users')),
    #GUI front end for our rest framework
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #token generation path api token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #endpoint api token refresh
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
