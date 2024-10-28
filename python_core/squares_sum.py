def squares_sum(n):
    result = 0

    for i in range(1, n + 1):
        result += i ** 2

    return result



print(squares_sum(3))
print(squares_sum(12))
print(squares_sum(13))
