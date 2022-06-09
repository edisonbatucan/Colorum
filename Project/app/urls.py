from django.db import router
from django.urls import path, include
from .views import SUVViewSet, PickUpViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('suvs', SUVViewSet, basename='suvs')
router.register('pickups', PickUpViewSet, basename='pickups')


urlpatterns = [
    
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    # # path('suvs/', suv_list),
    # path('suvs/', SUVAPIView.as_view()),
    # # path('suvs/<int:pk>/', suv_detail)
    # path('suvs/<int:id>/', SUVDetails.as_view()),
    # path('generic/suvs/<int:id>/', GenericAPIView.as_view()),
]
