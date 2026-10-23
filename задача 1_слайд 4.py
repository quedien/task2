import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):

    def test_zero_plus_five(self):
        result = add(0, 5)
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = add(-3, -7)
        self.assertEqual(result, -10)

    def test_mixed_numbers(self):
        result = add(10, -5)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()