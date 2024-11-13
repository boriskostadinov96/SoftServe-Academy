# Create a function that concatenates n input lists, where n is variable.

def concat(*args):
    answer = []
    for arg in args:
        for item in arg:
            answer.append(item)
    return answer


print(concat([1, 2, 3], [4, 5], [6, 7]))
