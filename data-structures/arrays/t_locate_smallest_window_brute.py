import unittest

class TestSmallestWindow(unittest.TestCase):
    
    def test_smallest_window(self):
        def setUp(self):
            self.arr1 = SmallestWindow([3, 7, 5, 6, 9])
        
        def test_smallest_window(self):
            self.assertEqual(self.arr1.window, (1, 3))


class SmallestWindow:
    def __init__(self, arr):
        self.arr = arr
        
    @property
    def window(array):
        left, right = None, None
        s = sorted(array)

        for i in range(len(array)):
            if array[i] != s[i] and left is None:
                left = i
            elif array[i] != s[i]:
                right = i
        return left, right
    
if __name__ == '__main__':
    unittest.main()
