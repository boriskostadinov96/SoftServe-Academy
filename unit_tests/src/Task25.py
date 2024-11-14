# A pandigital number contains all digits (0-9) at least once. Write a function that takes an integer, returning True if the integer is pandigital, and False otherwise.

def pandigital_numbers(number):
    for i in range(10):
        if str(i) in str(number):
            return True
        else:
            return False


print(pandigital_numbers(112233445566778899))
