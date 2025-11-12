import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_with_negative(self):
        self.assertEqual(self.calc.add(-3, 5), 2)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 7), 7)
    
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(4, 10), -6)

    def test_multiply_basic(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_with_negative(self):
        self.assertEqual(self.calc.multiply(-2, 5), -10)

    def test_divide_basic(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

    def test_divide_with_remainder(self):
        self.assertEqual(self.calc.divide(7, 3), 2)

    def test_modulo_basic(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)

    def test_modulo_exact(self):
        self.assertEqual(self.calc.modulo(6, 3), 0)

if __name__ == '__main__':
    unittest.main() 