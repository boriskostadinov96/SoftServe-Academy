def chatroom_status(users_list):
    result = ""

    if not users_list:
        result = "no one online"

    elif len(users_list) == 1:
        result = f"{users_list[0]} online"

    elif len(users_list) == 2:
        result = f"{users_list[0]} and {users_list[1]} online"

    else:
        result = f"{users_list[0]}, {users_list[1]} and {len(users_list) - 2} more online"

    return result


print(chatroom_status([]))
print(chatroom_status(["paRIE_to"]))
print(chatroom_status(["s234f", "mailbox2"]))
print(chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"]))
