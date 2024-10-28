def sum_even_nums_in_range(start, stop):
    result = 0

    for num in range(start, stop + 1):
        if num % 2 == 0:
            result += num

    return result


print(sum_even_nums_in_range(51, 150))
print(sum_even_nums_in_range(63, 97))
