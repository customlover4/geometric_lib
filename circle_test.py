import unittest
import math
import circle

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = circle.area(5)
        self.assertEqual(res, math.pi * 5 * 5)

    def test_neg_mul(self):
        res = circle.area(-5)
        self.assertEqual(res, 0)

    def test_neg_per(self):
        res = circle.perimeter(-11)
        self.assertEqual(res, 0)
    
    def test_good_per(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 2 * math.pi * 5)
    
    def test_zero_per(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
