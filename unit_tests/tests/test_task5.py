import unittest

from src.Task5 import list_of_multiples


class TestListOfMultiples(unittest.TestCase):
    def test_standard_cases(self):
        self.assertEqual(list_of_multiples(7, 5), [7, 14, 21, 28, 35])
        self.assertEqual(list_of_multiples(3, 4), [3, 6, 9, 12])
        self.assertEqual(list_of_multiples(5, 3), [5, 10, 15])

    def test_single_multiple(self):
        self.assertEqual(list_of_multiples(10, 1), [10])

    def test_zero_multiple(self):
        self.assertEqual(list_of_multiples(0, 5), [0, 0, 0, 0, 0])

    def test_large_number(self):
        self.assertEqual(list_of_multiples(1000, 3), [1000, 2000, 3000])


if __name__ == "__main__":
    unittest.main()
