def count_overlapping(list_intervals, point):
    count = 0

    for interval in list_intervals:
        if interval[0] <= point <= interval[1]:
            count += 1

    return count


print(count_overlapping([[1, 2], [2, 3], [3, 4]], 5))
print(count_overlapping([[1, 2], [5, 6], [5, 7]], 5))
print(count_overlapping([[1, 2], [5, 8], [6, 9]], 7))
