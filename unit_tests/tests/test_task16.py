import unittest
from src.Task16 import intersecting_intervals


class TestIntersectingIntervalsFunction(unittest.TestCase):

    def test_point_inside_multiple_intervals(self):
        self.assertEqual(intersecting_intervals([[1, 2], [5, 6], [5, 7]], 5), 2)

    def test_point_on_boundary(self):
        self.assertEqual(intersecting_intervals([[1, 3], [4, 7], [5, 7]], 3), 1)

    def test_point_outside_intervals(self):
        self.assertEqual(intersecting_intervals([[1, 2], [5, 6], [5, 7]], 8), 0)

    def test_point_on_multiple_boundaries(self):
        self.assertEqual(intersecting_intervals([[1, 3], [2, 5], [4, 6]], 3), 2)

    def test_single_interval(self):
        self.assertEqual(intersecting_intervals([[2, 5]], 4), 1)

    def test_point_at_interval_end(self):
        self.assertEqual(intersecting_intervals([[1, 2], [3, 5], [6, 8]], 2), 1)

    def test_empty_intervals(self):
        self.assertEqual(intersecting_intervals([], 5), 0)


if __name__ == "__main__":
    unittest.main()
