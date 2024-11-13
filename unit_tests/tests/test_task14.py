import unittest
from src.Task14 import sum_fractions


class TestSumFractionsFunction(unittest.TestCase):

    def test_standard_case(self):
        self.assertEqual(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]), 11)

    def test_single_fraction(self):
        self.assertEqual(sum_fractions([[5, 2]]), 3)

    def test_mixed_fractions(self):
        self.assertEqual(sum_fractions([[1, 3], [1, 6], [1, 2]]), 1)

    def test_large_numbers(self):
        self.assertEqual(sum_fractions([[100000, 3], [200000, 5]]), 73333)

    def test_zero_numerators(self):
        self.assertEqual(sum_fractions([[0, 1], [0, 5], [0, 2]]), 0)

    def test_whole_numbers_as_fractions(self):
        self.assertEqual(sum_fractions([[6, 3], [4, 2], [10, 5]]), 6)


if __name__ == "__main__":
    unittest.main()
