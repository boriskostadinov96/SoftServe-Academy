import unittest

from src.Task22 import num_of_sublists


class TestNumOfSublists(unittest.TestCase):

    def test_no_sublists(self):
        self.assertEqual(num_of_sublists([1, 2, 3]), 0)
        self.assertEqual(num_of_sublists(['a', 'b', 'c']), 0)

    def test_some_sublists(self):
        self.assertEqual(num_of_sublists([1, [2, 3], 4, [5, 6]]), 2)
        self.assertEqual(num_of_sublists([[1], 2, [3, 4], 'a']), 2)

    def test_all_sublists(self):
        self.assertEqual(num_of_sublists([[1, 2], [3, 4], [5, 6]]), 3)
        self.assertEqual(num_of_sublists([[], [], []]), 3)

    def test_empty_list(self):
        self.assertEqual(num_of_sublists([]), 0)

    def test_nested_sublists(self):
        self.assertEqual(num_of_sublists([[1, [2, 3]], [4, 5], 6]), 2)


if __name__ == '__main__':
    unittest.main()
