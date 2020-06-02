def factorization(user_input):

    list_elements = []
    for elements in range(1,user_input + 1):
        if user_input % elements == 0:
            list_elements.append(elements)
    return list_elements

user_input = int(input('Type a number: '))
print(factorization(user_input))