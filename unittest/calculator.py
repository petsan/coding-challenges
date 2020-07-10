import unittest

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        result = Calculator.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(-1, -1), -2)
        
    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 5), 5)
        self.assertEqual(Calculator.subtract(-1, 1), -2)
        self.assertEqual(Calculator.subtract(-1, -1), 0)
        
    def test_multiply(self):
        self.assertEqual(Calculator.multiply(10, 5), 50)
        self.assertEqual(Calculator.multiply(-1, 1), -1)
        self.assertEqual(Calculator.multiply(-1, -1), 1)
        
    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 5), 2)
        self.assertEqual(Calculator.divide(-1, 1), -1)
        self.assertEqual(Calculator.divide(-1, -1), 1)
        self.assertRaises(ValueError, Calculator.divide, 10, 0)

        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)

class Calculator:
    
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            raise ValueError('cannot divide by 0')

        return x / y

if __name__ == '__main__':
    unittest.main()
                         
        