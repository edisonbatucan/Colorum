from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

# class SUV(models.Model):
#     car_name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     num_seats = models.IntegerField()
#     wheel_size = models.CharField(max_length=50)

#     def __str__(self):
#         return self.car_name

class Post(models.Model):

    options = (
        ('suv','SUV'),
        ('sports car','Sports Car'),
        ('van','Van'),
        ('pickup','PickUp')
    )
    person = models.ForeignKey(
        User, on_delete= models.CASCADE, related_name='vehicle_post'
    )
    car_name = models.CharField(max_length=100)
    price = models.IntegerField()
    num_seats = models.IntegerField()
    wheel_size = models.CharField(max_length=50)
    
    car_type= models.CharField(
        max_length=10, choices=options, default='SUV'
    )
    
    objects = models.Manager()#default manager

    class Meta:
        ordering = ('-price',)
    
    def __str__(self):
        return self.car_name