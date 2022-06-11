from .views import VehicleList
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


app_name ='vehicle_api'

router = DefaultRouter()
router.register('', VehicleList, basename='vehicle')
urlpatterns = router.urls


# urlpatterns =[
#     path('<int:pk>/', VehicleDetail.as_view(), name='detailcreate'),
#     path('', VehicleList.as_view(), name='listcreate'),
# ]