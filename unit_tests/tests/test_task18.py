import unittest

from src.Task18 import square_patch


class TestSquarePatchFunction(unittest.TestCase):

    def test_square_patch_with_zero(self):
        self.assertEqual(square_patch(0), [])

    def test_square_patch_with_one(self):
        self.assertEqual(square_patch(1), [[1]])

    def test_square_patch_with_two(self):
        self.assertEqual(square_patch(2), [[2, 2], [2, 2]])

    def test_square_patch_with_three(self):
        self.assertEqual(square_patch(3), [[3, 3, 3], [3, 3, 3], [3, 3, 3]])

    def test_square_patch_with_large_value(self):
        self.assertEqual(square_patch(4), [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]])


if __name__ == "__main__":
    unittest.main()
