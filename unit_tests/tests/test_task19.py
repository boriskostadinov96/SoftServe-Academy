import unittest

from src.Task19 import oddish_or_evenish


class TestOddishOrEvenish(unittest.TestCase):

    def test_oddish(self):
        self.assertEqual(oddish_or_evenish(43), "Oddish")
        self.assertEqual(oddish_or_evenish(101), "Oddish")
        self.assertEqual(oddish_or_evenish(5), "Oddish")

    def test_evenish(self):
        self.assertEqual(oddish_or_evenish(22), "Evenish")
        self.assertEqual(oddish_or_evenish(12), "Evenish")
        self.assertEqual(oddish_or_evenish(8), "Evenish")

    def test_large_number(self):
        self.assertEqual(oddish_or_evenish(123456789), "Oddish")

    def test_single_digit(self):
        self.assertEqual(oddish_or_evenish(0), "Evenish")
        self.assertEqual(oddish_or_evenish(1), "Oddish")
        self.assertEqual(oddish_or_evenish(9), "Oddish")


if __name__ == "__main__":
    unittest.main()
