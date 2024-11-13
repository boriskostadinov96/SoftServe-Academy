import unittest

from src.Task17 import progress_day


class TestProgressDayFunction(unittest.TestCase):

    def test_progress_day_with_increasing_miles(self):
        self.assertEqual(progress_day([1, 2, 3, 4, 5]), 4)

    def test_progress_day_with_decreasing_miles(self):
        self.assertEqual(progress_day([5, 4, 3, 2, 1]), 0)

    def test_progress_day_with_mixed_increase_and_decrease(self):
        self.assertEqual(progress_day([10, 11, 12, 9, 10]), 3)

    def test_progress_day_with_all_equal_miles(self):
        self.assertEqual(progress_day([5, 5, 5, 5, 5]), 0)

    def test_progress_day_with_single_value(self):
        self.assertEqual(progress_day([7]), 0)

    def test_progress_day_with_large_values(self):
        self.assertEqual(progress_day([100, 150, 200, 250, 300]), 4)

    def test_progress_day_with_decreasing_then_increasing_miles(self):
        self.assertEqual(progress_day([100, 90, 80, 100, 120]), 2)


if __name__ == "__main__":
    unittest.main()
