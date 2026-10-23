import unittest

def check_age(age):
    if age < 0:
        return "Ошибка"
    elif age < 18:
        return "Несовершеннолетний"
    elif age < 60:
        return "Взрослый"
    else:
        return "Пенсионер"

class TestAge(unittest.TestCase):

    def test_age_error(self):
        self.assertEqual(check_age(-5), "Ошибка")

    def test_age_minor(self):
        self.assertEqual(check_age(14), "Несовершеннолетний")

    def test_age_adult(self):
        self.assertEqual(check_age(47), "Взрослый")

    def test_age_pensioner(self):
        self.assertEqual(check_age(65), "Пенсионер")

if __name__ == '__main__':
    unittest.main()