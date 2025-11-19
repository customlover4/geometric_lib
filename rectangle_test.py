import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_neg_mul(self):
        res = rectangle.area(-10, 10)
        self.assertEqual(res, 0)

    def test_neg_per(self):
        res = rectangle.perimeter(-11, 22)
        self.assertEqual(res, 0)
    
    def test_good_per(self):
        res = rectangle.perimeter(10, 20)
        self.assertEqual(res, 60)
    
    def test_zero_per(self):
        res = rectangle.perimeter(0, 10)
        self.assertEqual(res, 0)
