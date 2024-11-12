import unittest
from src.Task10 import stupid_addition


class TestStupidAddition(unittest.TestCase):

    def test_addition_with_strings(self):
        self.assertEqual(stupid_addition("3", "4"), 7)
        self.assertEqual(stupid_addition("10", "5"), 15)

    def test_addition_with_integers(self):
        self.assertEqual(stupid_addition(3, 4), "34")
        self.assertEqual(stupid_addition(100, 20), "10020")

    def test_mixed_types(self):
        self.assertEqual(stupid_addition("1", 2), "12")
        self.assertEqual(stupid_addition(1, "2"), "12")

    def test_invalid_type(self):
        self.assertIsNone(stupid_addition("1", None))
        self.assertIsNone(stupid_addition(None, 2))
        self.assertIsNone(stupid_addition("one", "two"))

    def test_mixed_invalid(self):
        self.assertIsNone(stupid_addition("10", 3.5))
        self.assertIsNone(stupid_addition(2.5, "3"))


if __name__ == "__main__":
    unittest.main()
