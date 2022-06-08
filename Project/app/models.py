from turtle import mode
from django.db import models

# Create your models here.


class SUV(models.Model):
    car_name = models.CharField(max_length=100)
    price = models.IntegerField()
    num_seats = models.IntegerField()
    wheel_size = models.CharField(max_length=50)

    def __str__(self):
        return self.car_name
