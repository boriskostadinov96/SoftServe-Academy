import unittest
from src.Task11 import is_repdigit


class TestIsRepdigit(unittest.TestCase):

    def test_positive_repdigit(self):
        self.assertTrue(is_repdigit(111))
        self.assertTrue(is_repdigit(9999))
        self.assertTrue(is_repdigit(0))

    def test_non_repdigit(self):
        self.assertFalse(is_repdigit(123))
        self.assertFalse(is_repdigit(1020))

    def test_negative_number(self):
        self.assertFalse(is_repdigit(-111))

    def test_large_repdigit(self):
        self.assertTrue(is_repdigit(88888888))

    def test_single_digit_non_repdigit(self):
        self.assertTrue(is_repdigit(7))


if __name__ == "__main__":
    unittest.main()
