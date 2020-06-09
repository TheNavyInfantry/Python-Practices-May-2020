def vote_convertor():
    result = []

    values = user_input.split()
    for each in values:
        if 'k' not in each:
            result.append(int(each))
        else:
            values_2 = each.replace('k','00').replace('.','')
            result.append(int(values_2))

        return result

user_input = input('Enter here: ')
print(vote_convertor())