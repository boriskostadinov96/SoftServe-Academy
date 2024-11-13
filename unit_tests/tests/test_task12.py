import unittest
from src.Task12 import concat


class TestConcatFunction(unittest.TestCase):

    def test_multiple_non_empty_lists(self):
        self.assertEqual(concat([1, 2, 3], [4, 5], [6, 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_single_list(self):
        self.assertEqual(concat([1, 2, 3]), [1, 2, 3])

    def test_no_lists(self):
        self.assertEqual(concat(), [])

    def test_with_empty_list(self):
        self.assertEqual(concat([], [1, 2, 3], [], [4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(concat([], []), [])

    def test_different_data_types(self):
        self.assertEqual(concat(['a', 'b'], [1, 2, 3], [True, False]), ['a', 'b', 1, 2, 3, True, False])

    def test_nested_lists(self):
        self.assertEqual(concat([[1, 2]], [[3, 4]], [5]), [[1, 2], [3, 4], 5])


if __name__ == "__main__":
    unittest.main()
