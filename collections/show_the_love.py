def show_the_love(share_list):
    min_index = share_list.index(min(share_list))
    total_to_add = 0

    for i in range(len(share_list)):
        if i != min_index:
            reduction = share_list[i] * 0.25
            share_list[i] -= reduction
            total_to_add += reduction

    share_list[min_index] += total_to_add

    share_list = [int(x) if x.is_integer() else x for x in share_list]

    return share_list


print(show_the_love([4, 1, 4]))
print(show_the_love([16, 10, 8]))
print(show_the_love([2, 100]))
