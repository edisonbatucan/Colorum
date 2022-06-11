from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'vehicle'

urlpatterns = [
    path('', TemplateView.as_view(template_name="vehicle/index.html")),
]
