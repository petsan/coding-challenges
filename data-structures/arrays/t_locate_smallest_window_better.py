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
        n = len(array)
        max_seen, min_seen = -float("inf"), float("inf")

        for i in range(n):
            max_seen = max(max_seen, array[i])
            if array[i] < max_seen:
                right = i

        for i in range(n - 1, -1, -1):
            min_seen = min(min_seen, array[i])
            if array[i] > min_seen:
                left = i

        return left, right
    
if __name__ == '__main__':
    unittest.main()
