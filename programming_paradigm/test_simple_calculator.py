import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator (unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 7), -2)
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-5, 7), -12)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 7), 35)
        self.assertEqual(self.calc.multiply(-110, 5), -550)
        self.assertEqual(self.calc.multiply(-2, -7), 14)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(10, -5), -2)
        self.assertEqual(self.calc.divide(-7, 2), -3.5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
