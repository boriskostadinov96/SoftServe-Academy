import unittest

from src.Task7 import lines_are_parallel


class TestLinesAreParallel(unittest.TestCase):

    def test_parallel_lines(self):
        self.assertTrue(lines_are_parallel([1, 2, 3], [2, 4, 6]))
        self.assertTrue(lines_are_parallel([1, -1, 3], [2, -2, 6]))

    def test_non_parallel_lines(self):
        self.assertFalse(lines_are_parallel([1, 2, 3], [1, 3, 5]))
        self.assertFalse(lines_are_parallel([2, 3, 4], [4, 2, 5]))

    def test_vertical_lines(self):
        self.assertTrue(lines_are_parallel([1, 0, 3], [2, 0, 5]))
        self.assertFalse(lines_are_parallel([1, 0, 3], [2, 3, 5]))
        self.assertFalse(lines_are_parallel([0, 0, 3], [0, 0, 5]))


if __name__ == "__main__":
    unittest.main()
