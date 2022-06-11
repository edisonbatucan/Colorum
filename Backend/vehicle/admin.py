from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Vehicle)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_name', 'price', 'num_seats', 'wheel_size', 'car_type')
