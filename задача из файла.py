import unittest

def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        return None
    bmi = weight / (height * height)
    return round(bmi, 1)

class TestBMI(unittest.TestCase):

    def test_normal_bmi(self):
        result = calculate_bmi(70, 1.75)
        self.assertEqual(result, 22.9)

    def test_zero_weight(self):
        result = calculate_bmi(0, 1.75)
        self.assertEqual(result, None)

    def test_negative_height(self):
        result = calculate_bmi(70, -1.75)
        self.assertEqual(result, None)

    def test_small_height(self):
        result = calculate_bmi(10, 0.5)
        self.assertEqual(result, 40.0)

if __name__ == '__main__':
    unittest.main()