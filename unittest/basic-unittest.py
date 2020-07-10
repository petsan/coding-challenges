import unittest

class TestCar(unittest.TestCase):
    
    def setUp(self):
        self.car_1 = Car('Jeep', 'Explorer')
        self.car_2 = Car('BMW', 'M3')
        
    def tearDown(self):
        pass
    
    def test_my_car(self):
        self.assertEqual(self.car_1.my_car, 'Jeep Explorer')
        self.assertEqual(self.car_2.my_car, 'BMW M3')

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    @property
    def my_car(self):
        return '{} {}'.format(self.make, self.model)

if __name__ == '__main__':
    unittest.main()
