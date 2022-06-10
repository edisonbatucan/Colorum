from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vehicle(models.Model):

    options = (
        ('suv','SUV'),
        ('sports car','Sports Car'),
        ('van','Van'),
        ('pickup','PickUp')
    )
    person = models.ForeignKey(
        User, on_delete= models.CASCADE)
    car_name = models.CharField(max_length=100)
    price = models.IntegerField()
    num_seats = models.IntegerField()
    wheel_size = models.CharField(max_length=50)
    car_type= models.CharField(
        max_length=10, choices=options, default='SUV'
    )

    class Meta:
        ordering = ('-price',)
    
    def __str__(self):
        return self.car_name