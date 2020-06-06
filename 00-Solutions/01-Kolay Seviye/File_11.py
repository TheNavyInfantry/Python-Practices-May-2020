
def max_min_calculator():

    limit = 4
    count = 0
    user_List = []

    while count < limit:
        user_Input = input('Type: ')
        user_List.append(user_Input)
        count += 1
        if count == limit:
            break

    return str(max(user_List))+ " " +str(min(user_List))

print(max_min_calculator())


