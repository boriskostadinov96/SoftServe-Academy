def get_budgets(lst_budgets):
    total = 0

    for person in lst_budgets:
        total += person['budget']
    return total


print(get_budgets([
    {"name": "John", "age": 21, "budget": 23000},
    {"name": "Steve", "age": 32, "budget": 40000},
    {"name": "Martin", "age": 16, "budget": 2700}
]))

print(get_budgets([
    {"name": "John", "age": 21, "budget": 29000},
    {"name": "Steve", "age": 32, "budget": 32000},
    {"name": "Martin", "age": 16, "budget": 1600}
]))
