def pops(pop_list):
    if not pop_list or max(pop_list) == 0:
        return pop_list

    center = pop_list.index(max(pop_list))
    max_val = pop_list[center]

    return [max(0, max_val - abs(i - center)) for i in range(len(pop_list))]


print(pops([0, 0, 0, 0, 4, 0, 0, 0, 0]))
print(pops([0, 0, 0, 3, 0, 0, 0]))
print(pops([0, 0, 2, 0, 0]))
print(pops([0]))
