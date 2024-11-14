# In the Code tab is a function which is meant to return how many uppercase letters there are in a list of various words. Fix the list comprehension so that the code functions normally!

def count_letters(lst):
    count = 0
    for word in lst:
        for letter in word:
            if letter.isupper():
                count = count + 1
    return count


print(count_letters(['SOLO', 'hello', 'Tea', 'wHat']))
