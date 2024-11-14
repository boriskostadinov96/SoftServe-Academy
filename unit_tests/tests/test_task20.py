import unittest

from src.Task20 import dice_game


class TestDiceGame(unittest.TestCase):

    def test_no_doubles(self):
        self.assertEqual(dice_game([(1, 2), (3, 4), (5, 6)]), 1 + 2 + 3 + 4 + 5 + 6)

    def test_doubles_in_first_round(self):
        self.assertEqual(dice_game([(1, 1), (3, 4), (5, 6)]), 0)

    def test_doubles_in_middle_round(self):
        self.assertEqual(dice_game([(3, 2), (2, 2), (5, 6)]), 0)

    def test_valid_game_no_doubles(self):
        self.assertEqual(dice_game([(6, 3), (4, 2), (1, 1)]), 0)

    def test_single_round_no_doubles(self):
        self.assertEqual(dice_game([(1, 4)]), 1 + 4)

    def test_single_round_with_doubles(self):
        self.assertEqual(dice_game([(3, 3)]), 0)


if __name__ == '__main__':
    unittest.main()
