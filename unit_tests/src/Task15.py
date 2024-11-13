# Create a function that returns the indices of all occurrences of an item in the list.

def element_in_list(lst, el):
    list = []
    for i in range(len(lst)):
        if lst[i] == el:
            list.append(i)
    return list


print(element_in_list([1, 5, 5, 2, 7], 5))
