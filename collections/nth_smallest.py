def nth_smallest(list_numbers, n):
    sorted_list = sorted(list_numbers)

    if n > len(sorted_list):
        return None
    return sorted_list[n - 1]


print(nth_smallest([1, 3, 5, 7], 1))
print(nth_smallest([1, 3, 5, 7], 3))
print(nth_smallest([1, 3, 5, 7], 5))
print(nth_smallest([7, 3, 5, 1], 2))
