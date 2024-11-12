import unittest

from src.Task4 import square_area


class TestSquareArea(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square_area(5), 50)
        self.assertEqual(square_area(10), 200)
        self.assertEqual(square_area(1), 2)
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(7), 98)


if __name__ == "__main__":
    unittest.main()
