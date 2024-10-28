def calculate_fuel(distance):
    fuel = distance * 10
    return int(max(fuel, 100))


print(calculate_fuel(15))
print(calculate_fuel(23.5))
print(calculate_fuel(3))
