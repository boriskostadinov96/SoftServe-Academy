def identical_filter(words):
    result = []

    for word in words:
        unique_chars = set(word)

        if len(unique_chars) == 1:
            result.append(word)
    return result


print(identical_filter(["aaaaaa", "bc", "d", "eeee", "xyz"]))
print(identical_filter(["88", "999", "22", "545", "133"]))
print(identical_filter(["xxxxo", "oxo", "xox", "ooxxoo", "oxo"]))
