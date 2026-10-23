import unittest

def is_positive(number):
    return number > 0

class TestPositive(unittest.TestCase):

    def test_five_is_positive(self):
        self.assertTrue(is_positive(5))

    def test_three_is_not_positive(self):
        self.assertFalse(is_positive(-3))

    def test_zero_is_not_positive(self):
        self.assertFalse(is_positive(0))

if __name__ == '__main__':
    unittest.main()