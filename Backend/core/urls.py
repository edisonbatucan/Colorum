from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
=======
>>>>>>> cfeec00b6b0276e891dcaa192fa7c22a56a03dfb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehicle.urls', namespace='vehicle')),
    path('api/', include('vehicle_api.urls', namespace='vehicle_api')),
<<<<<<< HEAD
    path('api/user/', include('users.urls', namespace='users')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
=======
>>>>>>> cfeec00b6b0276e891dcaa192fa7c22a56a03dfb
]
