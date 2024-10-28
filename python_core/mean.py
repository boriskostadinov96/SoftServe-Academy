def mean(number):
    digits = [int(digit) for digit in str(number)]
    total_sum = sum(digits)

    return total_sum // len(digits)


print(mean(42))
print(mean(12345))
print(mean(666))
