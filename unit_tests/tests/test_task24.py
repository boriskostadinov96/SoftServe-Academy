import unittest

from src.Task24 import count_letters


class TestCountLetters(unittest.TestCase):

    def test_mixed_case_words(self):
        self.assertEqual(count_letters(['SOLO', 'hello', 'Tea', 'wHat']), 6)

    def test_all_uppercase_words(self):
        self.assertEqual(count_letters(['HELLO', 'WORLD', 'TEST']), 12)

    def test_all_lowercase_words(self):
        self.assertEqual(count_letters(['hello', 'world', 'test']), 0)

    def test_empty_list(self):
        self.assertEqual(count_letters([]), 0)

    def test_single_uppercase_word(self):
        self.assertEqual(count_letters(['PYTHON']), 6)

    def test_mixed_words_with_numbers(self):
        self.assertEqual(count_letters(['A1B2C3', 'XyZ9', '123']), 5)


if __name__ == '__main__':
    unittest.main()
