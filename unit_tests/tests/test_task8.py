import unittest

from src.Task8 import volume


class TestVolumeOfSphericalShell(unittest.TestCase):

    def test_standard_case(self):
        self.assertEqual(volume(3, 2), 79.587)

    def test_zero_inner_radius(self):
        self.assertEqual(volume(5, 0), 523.599)

    def test_equal_radii(self):
        self.assertEqual(volume(4, 4), 0.0)

    def test_large_difference_in_radii(self):
        self.assertEqual(volume(1000, 1), 4188790200.598)

    def test_small_difference_in_radii(self):
        self.assertEqual(volume(2.001, 2), 0.016)


if __name__ == "__main__":
    unittest.main()
