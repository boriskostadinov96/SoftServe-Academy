# Create a function that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them.

def stupid_addition(num1, num2):
    if type(num1) == int and type(num2) == int:
        return str(num1) + str(num2)

    elif type(num1) == str and type(num2) == str:
        try:
            return int(num1) + int(num2)
        except ValueError:
            return None

    elif type(num1) == str and type(num2) == int:
        return str(num1) + str(num2)

    elif type(num1) == int and type(num2) == str:
        return str(num1) + str(num2)

    else:
        return None


print(stupid_addition("1", 2))
