def probability(numbers_list, n):
    favorable_outcomes = sum(1 for number in numbers_list if number >= n)
    probability_percentage = (favorable_outcomes / len(numbers_list)) * 100
    return round(probability_percentage, 1)

print(probability([5, 1, 8, 9], 6))
print(probability([7, 4, 17, 14, 12, 3], 16))
print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))
