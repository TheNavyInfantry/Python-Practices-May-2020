import math

def pow_finder(x,y):
    return round(int(math.log(x, y)))

x,y = input('Enter result-x and base-y to find the power: ').split()
x = int(x)
y = int(y)

print(pow_finder(x,y))