import unittest

from src.Task21 import sastry_numbers


class TestSastryNumbers(unittest.TestCase):

    def test_sastry_number(self):
        self.assertTrue(sastry_numbers(183))
        self.assertTrue(sastry_numbers(328))
        self.assertTrue(sastry_numbers(528))

    def test_non_sastry_number(self):
        self.assertFalse(sastry_numbers(5))
        self.assertFalse(sastry_numbers(50))
        self.assertFalse(sastry_numbers(100))

    def test_edge_cases(self):
        self.assertFalse(sastry_numbers(1))
        self.assertFalse(sastry_numbers(2))
        self.assertTrue(sastry_numbers(0))


if __name__ == '__main__':
    unittest.main()
