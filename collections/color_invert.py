def color_invert(rgb):
    return tuple(255 - value for value in rgb)


print(color_invert((255, 255, 255)))
print(color_invert((0, 0, 0)))
print(color_invert((165, 170, 221)))