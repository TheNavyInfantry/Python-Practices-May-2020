def reverse_input(sentence):
    if len(sentence) <= 5:
        return 'Type more than 5 characters!'

    elif len(sentence) >= 5:
        for spaces in sentence:
            if spaces.isspace() >= 1:
                return sentence[::-1]
            else:
                break

        return sentence[::-1]

user_input = input('Type your sentence: ')
print(reverse_input(user_input))
