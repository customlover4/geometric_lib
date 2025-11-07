import unittest
import square

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = square.area(0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_neg_mul(self):
        res = square.area(-5)
        self.assertEqual(res, 0)

    def test_neg_per(self):
        res = square.perimeter(-11)
        self.assertEqual(res, 0)
    
    def test_good_per(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)
    
    def test_zero_mul(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
