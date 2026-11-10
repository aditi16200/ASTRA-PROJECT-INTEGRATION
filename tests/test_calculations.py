import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import calculations


class TestCalculations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculations.add(10, 5), 15)

    def test_multiplication(self):
        self.assertEqual(calculations.multiply(10, 5), 50)

    def test_subtraction(self):
        self.assertEqual(calculations.subtract(10, 5), 5)

    def test_division(self):
        self.assertEqual(calculations.divide(10, 5), 2)


if __name__ == "__main__":
    unittest.main()