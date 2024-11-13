# Create a function that takes an integer and outputs an n x n square solely consisting of the integer n.

def square_patch(n):
    result = []
    for i in range(n):
        result.append([n] * n)

    return result


print(square_patch(0))
