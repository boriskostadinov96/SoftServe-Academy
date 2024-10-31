def index_of_caps(word):
    upper_indices = []

    for index, letter in enumerate(word):
        if letter.isupper():
            upper_indices.append(index)

    return upper_indices


print(index_of_caps("eQuINoX"))
print(index_of_caps("determine"))
print(index_of_caps("STRIKE"))
print(index_of_caps("sUn"))