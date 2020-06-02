def check_func(user_input):
    if user_input == user_input.lower() or user_input == user_input.upper():
        return True
    else:
        return False

user_input = str(input("Type a word: "))
print(check_func(user_input))
