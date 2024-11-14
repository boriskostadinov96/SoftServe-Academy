# Your job is to create a function, that takes 3 numbers: a, b, c and returns True if the last digit of (the last digit of a * the last digit of b) = the last digit of c. Check examples for explanation.

def last_digit(a, b, c):
    return a * b % 10 == c % 10


print(last_digit(12, 215, 2142))
