# Create a function that takes a list containing nested lists as an argument. Each sublist has 2 elements. The first element is the numerator and the second element is the denominator. Return the sum of the fractions rounded to the nearest whole number.

def sum_fractions(lst):
    total = 0
    for i in lst:
        total += i[0] / i[1]
    return round(total)


print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))
