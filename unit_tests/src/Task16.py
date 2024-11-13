# in a list of intervals and returns how many intervals overlap with a given point.
# An interval overlaps a particular point if the point exists inside the interval, or on the interval's boundary. For example the point 3 overlaps with the interval [2, 4] (it is inside) and [2, 3] (it is on the boundary).

def intersecting_intervals(interval, point):
    count = 0
    for x in interval:
        if point >= x[0] and point <= x[1]:
            count += 1
    return count


print(intersecting_intervals([[1, 2], [5, 6], [5, 7]], 5))
