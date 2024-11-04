def check(dict1, dict2, key_ch):
    has_key1 = key_ch in dict1
    has_key2 = key_ch in dict2

    if has_key1 and has_key2:
        if dict1[key_ch] == dict2[key_ch]:
            return True

        return "Not the same"

    elif has_key1 or has_key2:
        return "One's empty"

    return "One's empty"


dict_first = {"sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright"}
dict_second = {"people": 12, "sun": "star", "book": "bad"}

print(check(dict_first, dict_second, "horde"))
print(check(dict_first, dict_second, "people"))
print(check(dict_first, dict_second, "sun"))
