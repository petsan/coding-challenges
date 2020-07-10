import unittest

class TestPerson(unittest.TestCase):
    
    def setUp(self):
        self.person_1 = Person('Jane', 'Doe')
        self.person_2 = Person('Jim', 'James')
    
    def tearDown(self):
        pass
        
    def test_fullname(self):
        self.assertEqual(self.person_1.fullname, 'Jane Doe')
        self.assertEqual(self.person_2.fullname, 'Jim James')
        
        self.person_1.first = 'Jenny'
        self.person_2.first = 'Chris'
        self.assertEqual(self.person_1.fullname, 'Jenny Doe')
        self.assertEqual(self.person_2.fullname, 'Chris James')
       
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
if __name__ == '__main__':
    unittest.main()
