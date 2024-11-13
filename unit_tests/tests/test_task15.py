import unittest
from src.Task15 import element_in_list


class TestElementInListFunction(unittest.TestCase):

    def test_multiple_occurrences(self):
        self.assertEqual(element_in_list([1, 5, 5, 2, 7], 5), [1, 2])

    def test_single_occurrence(self):
        self.assertEqual(element_in_list([1, 3, 4, 7], 4), [2])

    def test_no_occurrences(self):
        self.assertEqual(element_in_list([1, 2, 3, 4], 5), [])

    def test_all_occurrences(self):
        self.assertEqual(element_in_list([6, 6, 6, 6], 6), [0, 1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(element_in_list([], 3), [])

    def test_varied_data(self):
        self.assertEqual(element_in_list(["a", 1, "b", "a"], "a"), [0, 3])


if __name__ == "__main__":
    unittest.main()
