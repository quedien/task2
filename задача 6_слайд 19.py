import unittest

def word_lengths(sentence):
    wd = {}
    s = sentence.split()
    for i in s:
        wd[i] = len(i)
    return wd

class TestWordLengths(unittest.TestCase):

    def test_normal_phrase(self):
        result = word_lengths("I love Python")
        self.assertEqual(result, {"I": 1, "love": 4, "Python": 6})

    def test_single_word(self):
        result = word_lengths("Hello")
        self.assertEqual(result, {"Hello": 5})

    def test_empty_string(self):
        result = word_lengths("")
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()