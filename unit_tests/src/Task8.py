# The volume of a spherical shell is the difference between the enclosed volume of the outer sphere and the enclosed volume of the inner sphere:

# Create a function that takes r1 and r2 as arguments and returns the volume of a spherical shell rounded to the nearest thousandth

from math import pi


def volume(r1, r2):
    result = 4 / 3 * pi * (r1 ** 3 - r2 ** 3)
    return round(abs(result), 3)
