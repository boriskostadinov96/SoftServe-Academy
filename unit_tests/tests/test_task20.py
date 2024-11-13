import unittest

from src.Task20 import dice_game


def test_dice_game():
    assert dice_game([(1, 2), (3, 4), (5, 6)]) == 21

    assert dice_game([(1, 1), (3, 4), (5, 6)]) == 0

    assert dice_game([(3, 2), (2, 2), (5, 6)]) == 0

    assert dice_game([(6, 3), (4, 2), (1, 1)]) == 0

    assert dice_game([(2, 2), (4, 4), (6, 6)]) == 0

    assert dice_game([(2, 3)]) == 5

    print("All tests passed!")


if __name__ == "__main__":
    unittest.main()
