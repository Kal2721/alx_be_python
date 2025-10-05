import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        self.calc = SimpleCalculator()

    # Test addition
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    # Test subtraction
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
    # Test multiplication
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
    # Test division
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
