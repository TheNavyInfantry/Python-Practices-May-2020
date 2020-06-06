def index_multiplier():
    limit = int(input('Type a limit: '))
    count = 0

    numbers = []
    while count < limit:
        user_Input = input('Enter your numbers: ')
        numbers.append(user_Input)
        count += 1
        print('Number list is: ',numbers)

    sum_List = []
    for value in numbers:
        operation = int(value) * numbers.index(value)
        sum_List.append(operation)
    print('Sum is: ',sum(sum_List))

index_multiplier()

