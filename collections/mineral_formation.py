def mineral_formation(stones):
    stalactites = any(stones[0])

    stalagmites = any(stones[-1])

    if stalactites and stalagmites:
        return "both"

    elif stalactites:
        return "stalactites"

    elif stalagmites:
        return "stalagmites"


print(mineral_formation([
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]))

print(mineral_formation([
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1]
]))

print(mineral_formation([
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1]
]))