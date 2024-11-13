# A repdigit is a positive number composed out of the same digit.
# Create a function that takes an integer and returns whether it's a repdigit or not.

def is_repdigit(a):
    return a >= 0 and len(set(str(a))) == 1
