import unittest

from src.Task23 import last_digit


class TestLastDigit(unittest.TestCase):

    def test_last_digit_match(self):
        self.assertTrue(last_digit(12, 215, 2142))
        self.assertTrue(last_digit(3, 7, 21))
        self.assertTrue(last_digit(6, 4, 24))
        self.assertTrue(last_digit(15, 25, 375))

    def test_last_digit_no_match(self):
        self.assertFalse(last_digit(13, 21, 123))
        self.assertFalse(last_digit(2, 5, 12))
        self.assertFalse(last_digit(8, 9, 71))

    def test_zero_cases(self):
        self.assertTrue(last_digit(0, 100, 0))
        self.assertFalse(last_digit(0, 5, 3))

    def test_large_numbers(self):
        self.assertTrue(last_digit(123456789, 987654321, 2468101214))
        self.assertFalse(
            last_digit(123456789, 987654321, 2468101215))


if __name__ == '__main__':
    unittest.main()
