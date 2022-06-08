from django.urls import path
from .views import suv_list, suv_detail, SUVAPIView, SUVDetails

urlpatterns = [
    # path('suvs/', suv_list),
    path('suvs/', SUVAPIView.as_view()),
    # path('suvs/<int:pk>/', suv_detail)
    path('suvs/<int:id>/', SUVDetails.as_view()),
]
