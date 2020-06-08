def find_Middle(user):
    len_user = int(len(user))

    if (len_user % 2) == 0:
        lenght = int(len(user) / 2)
        print(user[lenght - 1:lenght + 1])

    elif (len_user % 2) != 0:
        lenght = int(len(user) / 2)
        print(user[lenght])

    return ''

sentence = input('Enter your sentence: ')
print(find_Middle(sentence))

