def apocalyptic_Number(n):

    calculation = pow(2, n)
    calculation = str(calculation)

    if calculation.count('666') == 0:
        print('Safe')
    elif calculation.count('666') == 1:
        print('Odd and there is only one')
    elif calculation.count('666') == 2:
        print('Even and there is two')
    elif calculation.count('666') == 3:
        print('Odd and there is three')

user_Input = int(input('Enter a number between 1-1000: '))
apocalyptic_Number(user_Input)