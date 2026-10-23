import unittest

def get_evens(numbers):
    return [n for n in numbers if n % 2 == 0]

class TestGetEvens(unittest.TestCase):

    def test_mixed_numbers(self):
        result = get_evens([1, 2, 3, 4, 5, 6])
        self.assertEqual(result, [2, 4, 6])

    def test_all_even(self):
        result = get_evens([2, 4, 6])
        self.assertEqual(result, [2, 4, 6])

    def test_all_odd(self):
        result = get_evens([1, 3, 5])
        self.assertEqual(result, [])

    def test_empty_list(self):
        result = get_evens([])
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()