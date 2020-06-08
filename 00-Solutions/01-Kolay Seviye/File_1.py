def pow_calculate(x,y):
    process = pow(x,y)
    return process

x,y = input("Type 2 numbers: ").split()
x = int(x)
y = int(y)

print(pow_calculate(x,y))

