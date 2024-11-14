import unittest

from src.Task25 import pandigital_numbers


class TestPandigitalNumbers(unittest.TestCase):

    def test_pandigital_number(self):
        self.assertTrue(pandigital_numbers(1023456789))

    def test_non_pandigital_number_missing_digits(self):
        self.assertFalse(pandigital_numbers(12345678))

    def test_large_pandigital_number(self):
        self.assertTrue(pandigital_numbers(12345678901234567890))

    def test_repeated_digits_not_pandigital(self):
        self.assertFalse(pandigital_numbers(112233445566778899))

    def test_short_number(self):
        self.assertFalse(pandigital_numbers(123))

    def test_single_digit(self):
        self.assertFalse(pandigital_numbers(9))


if __name__ == '__main__':
    unittest.main()
