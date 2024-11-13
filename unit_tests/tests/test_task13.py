import unittest
from src.Task13 import empty_values


class TestEmptyValuesFunction(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(empty_values([1, 3, 5]), [0, 0, 0])

    def test_floats(self):
        self.assertEqual(empty_values([3.14, 2.17, 0.5]), [0.0, 0.0, 0.0])

    def test_strings(self):
        self.assertEqual(empty_values(['hello', 'world', '']), ['', '', ''])

    def test_booleans(self):
        self.assertEqual(empty_values([True, False, True]), [False, False, False])

    def test_lists(self):
        self.assertEqual(empty_values([[1, 'a'], [3, 4], []]), [[], [], []])

    def test_tuples(self):
        self.assertEqual(empty_values([(1, 2), (3,), ()]), [(), (), ()])

    def test_sets(self):
        self.assertEqual(empty_values([{1, 2}, {'a'}, set()]), [set(), set(), set()])

    def test_none(self):
        self.assertEqual(empty_values([None, None]), [None, None])

    def test_mixed_types(self):
        self.assertEqual(
            empty_values([1, 3.14, 'string', True, [1, 2], (3, 4), {5, 6}, None]),
            [0, 0.0, '', False, [], (), set(), None]
        )


if __name__ == "__main__":
    unittest.main()
