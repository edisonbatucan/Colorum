from urllib import response
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from vehicle.models import Vehicle
from django.contrib.auth.models import User

# Create your tests here.


class VehicleTests(APITestCase):

    def test_view_vehicles(self):
        url = reverse('vehicle_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_vehicle(self):
        self.testuser1 = User.objects.create_user(
            username = 'test_user1', password = '123456789'
        )

        data = {"person": 1, "car_name": "New Car", "price": 5, "num_seats": 3, "wheel_size": "17 in", "car_type": "suv"}
        url = reverse('vehicle_api:lsitcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #(person_id = 1, car_name='Car', price=50, num_seats=3, wheel_size='17 in', car_type='suv')
    