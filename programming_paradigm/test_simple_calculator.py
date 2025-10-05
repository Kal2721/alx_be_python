import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        self.calculator = SimpleCalculator()

    # Test addition
    def test_addition(self):
        self.asserEqual(self.calculator.add(2, 3), 5)
    # Test subtraction
    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
    # Test multiplication
    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(4, 3), 12)
    # Test division
    def test_division(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
