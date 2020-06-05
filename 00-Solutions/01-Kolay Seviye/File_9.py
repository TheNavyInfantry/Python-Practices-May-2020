import string

def alp_num_counter(user_input):
    alphabet = list(string.ascii_lowercase)
    numbers = list(range(0,10))

    counted_alphabet = 0
    counted_number = 0

    for each in user_input:
        if each in alphabet:
            counted_alphabet += 1
        elif ' ' in each:
            pass
        else:
            counted_number += 1


user_input=input('Type: ')
user_input = user_input.lower()
print(alp_num_counter({'Alphabet':counted_alphabet, 'Numbers':counted_number}))