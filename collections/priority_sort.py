def priority_sort(unsort_lst, pri_set):
    if not unsort_lst:
        return []

    priority_elements = []
    other_elements = []

    for num in unsort_lst:
        if num in pri_set:
            priority_elements.append(num)
        else:
            other_elements.append(num)

    priority_elements.sort()
    other_elements.sort()

    return priority_elements + other_elements


print(priority_sort([5, 4, 3, 2, 1], {2, 3}))
print(priority_sort([5, 4, 3, 2, 1], {3, 6}))
print(priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}))