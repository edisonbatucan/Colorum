from django.test import TestCase
from django.contrib.auth.models import User
from vehicle.models import Vehicle

# Create your tests here.

class Test_Create_Vehicle(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username = 'test_user1', password = '123456789'
        )
        test_vehicle = Vehicle.objects.create(person_id = 1, car_name='Car', price=50, num_seats=3, wheel_size='17 in', car_type='suv')
    
    def test_vehicle_content(self):
        vehicle = Vehicle.objects.get(id=1)
        person = f'{vehicle.person}'
        car_name = f'{vehicle.car_name}'
        price = f'{vehicle.price}'
        num_seats = f'{vehicle.num_seats}'
        wheel_size = f'{vehicle.wheel_size}'
        car_type = f'{vehicle.car_type}'
        self.assertEqual(person, 'test_user1')
        self.assertEqual(car_name, 'Car')
        self.assertEqual(price, '50')
        self.assertEqual(num_seats, '3')
        self.assertEqual(wheel_size, '17 in')
        self.assertEqual(car_type, 'suv')