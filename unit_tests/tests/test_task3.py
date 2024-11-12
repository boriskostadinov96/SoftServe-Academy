import unittest

from src.Task3 import solutions


class TestQuadraticSolutions(unittest.TestCase):

    def test_two_solutions(self):
        self.assertEqual(solutions(1, -3, 2), 2)
        self.assertEqual(solutions(1, 0, -4), 2)

    def test_one_solution(self):
        self.assertEqual(solutions(1, 2, 1), 1)
        self.assertEqual(solutions(4, 4, 1), 1)

    def test_no_solution(self):
        self.assertEqual(solutions(1, 0, 1), 0)
        self.assertEqual(solutions(5, 2, 3), 0)


if __name__ == "__main__":
    unittest.main()
