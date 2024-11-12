# Suppose you have a guest list of students and the country they are from, stored as key-value pairs in a dictionary.
GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}
# Write a function that takes in a name and returns a name tag, that should read:
# "Hi! I'm [name], and I'm from [country]."GUEST_LIST = {"Randy": "Germany", "Karla": "France", "Wendy": "Japan", "Norman": "England", "Sam": "Argentina"}
# If the name is not in the dictionary, return:
# "Hi! I'm a guest."

def greeting(name):
    if name in GUEST_LIST.keys():
        return "Hi! I'm " + name + ", and I'm from " + GUEST_LIST[name] + "."
    else:
        return "Hi! I'm a guest."


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greeting(name))
