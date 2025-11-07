import unittest
import triangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = triangle.area(5, 10)
        self.assertEqual(res, 5 * 10 / 2)

    def test_neg_mul(self):
        res = triangle.area(-5, 10)
        self.assertEqual(res, 0)

    def test_neg_per(self):
        res = triangle.perimeter(-11, -11, -10)
        self.assertEqual(res, 0)
    
    def test_good_per(self):
        res = triangle.perimeter(5, 5, 5)
        self.assertEqual(res, 15)
    
    def test_zero_mul(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
