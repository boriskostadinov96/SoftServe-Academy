def is_plural(word):
    if word.endswith("s"):
        return True

    return False
    

print(is_plural("changes"))
print(is_plural("change"))