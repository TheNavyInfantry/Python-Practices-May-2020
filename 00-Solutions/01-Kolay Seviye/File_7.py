
def centuryfromyear(year):
    if len(year) <= 3:
        converter = year[:1]
        converted = int(converter) + 1
        return "{}. Century".format(converted)
    else:
        converter = year[:2]
        converted = int(converter) + 1
        return "{}. Century".format(converted)

user_input=str(input("Type a year to convert it into the century: "))
print(centuryfromyear(user_input))