def find_Zip(text):
    counted = text.count('zip')
    if counted < 2:
        return -1
    else:
        first = text.find('zip')
        return text.find('zip',first+1)

user_input = input('Type here: ')
print(find_Zip(user_input))

