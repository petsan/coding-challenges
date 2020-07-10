import requests
import unittest
from unittest.mock import patch

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.emp_1 = Employee('Jane', 'Doe', 50000)
        self.emp_2 = Employee('Jim', 'James', 60000)
    
    def tearDown(self):
        pass
    
    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Jane.Doe@email.com')
        self.assertEqual(self.emp_2.email, 'Jim.James@email.com')
        
        self.emp_1.first = 'Jenny'
        self.emp_2.first = 'Chris'
        self.assertEqual(self.emp_1.email, 'Jenny.Doe@email.com')
        self.assertEqual(self.emp_2.email, 'Chris.James@email.com')
        
    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Jane Doe')
        self.assertEqual(self.emp_2.fullname, 'Jim James')
        
        self.emp_1.first = 'Jenny'
        self.emp_2.first = 'Chris'
        self.assertEqual(self.emp_1.fullname, 'Jenny Doe')
        self.assertEqual(self.emp_2.fullname, 'Chris James')
        
    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
        
    def test_monthly_schedule(self):
        with patch('requests.get') as mocked_get:
            # test passing case
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Doe/May')
            self.assertEqual(schedule, 'Success')
            
            # test failing case
            mocked_get.return_value.ok = False
            
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/James/June')
            self.assertEqual(schedule, 'Bad Response!')

class Employee:
    raise_amt = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

if __name__ == '__main__':
    unittest.main()
