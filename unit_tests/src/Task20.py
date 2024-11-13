# John is playing a dice game. The rules are as follows.
# 1.	Roll two dice.
# 2.	Add the numbers on the dice together.
# 3.	Add the total to your overall score.
# 4.	Repeat this for three rounds.
# But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!
# Create a function that takes in a list of tuples as input, and return John's score after his game has ended.

def dice_game(point):
    result = 0
    for a, b in point:
        if a == b:
            return 0
        result += a + b
    return result


print(dice_game([(1, 2), (3, 4), (5, 6)]))
