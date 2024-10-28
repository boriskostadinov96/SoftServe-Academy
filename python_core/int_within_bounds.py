def int_within_bounds(number, lower_bound, upper_bound):
    if not isinstance(number, int):
        return False

    return lower_bound <= number < upper_bound


print(int_within_bounds(3, 1, 9))
print(int_within_bounds(6, 1, 6))
print(int_within_bounds(4.5, 3, 8))
