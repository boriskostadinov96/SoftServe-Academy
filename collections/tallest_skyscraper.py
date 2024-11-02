def tallest_skyscraper(sky_list):
    if not sky_list:
        return 0

    rows = len(sky_list)
    cols = len(sky_list[0])

    max_height = 0

    for col in range(cols):
        height = sum(sky_list[row][col] for row in range(rows))
        max_height = max(max_height, height)

    return max_height


print(tallest_skyscraper([
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
]))

print(tallest_skyscraper([
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
]))

print(tallest_skyscraper([
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]))
