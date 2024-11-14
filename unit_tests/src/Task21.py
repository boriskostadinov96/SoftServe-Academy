# In this challenge, you have to establish if a given integer n is a Sastry number. If the number resulting from the concatenation of an integer n with its successor is a perfect square, then n is a Sastry Number.
# Given a positive integer n, implement a function that returns True if n is a Sastry number, or False if it's not.

import math


def sastry_numbers(n):
    b = int(str(n) + str(n + 1))
    if math.sqrt(b) % 1 == 0:
        return True
    else:
        return False


print(sastry_numbers(183))
