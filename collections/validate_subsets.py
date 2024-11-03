def validate_subsets(subsets, one_set):
    one_set = set(one_set)

    for subset in subsets:
        if not set(subset).issubset(one_set):
            return False

    return True


print(validate_subsets([[1, 2], [2, 3], [1, 3]], [1, 2, 3]))
print(validate_subsets([[1, 2, 3], [2], [3], []], [1, 2, 3]))
print(validate_subsets([[1, 2], [2, 3], [1, 4]], [1, 2, 3]))
print(validate_subsets([[1, 2, 3, 4]], [1, 2, 3]))
