import unittest

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x):
        self.result += x

    def subtract(self, x):
        self.result -= x

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_subtract_from_zero(self):
        self.calc.subtract(3)
        self.assertEqual(self.calc.result, -3)

    def test_add_then_subtract(self):
        self.calc.add(10)
        self.calc.subtract(3)
        self.assertEqual(self.calc.result, 7)

if __name__ == '__main__':
    unittest.main()