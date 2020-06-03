def animals(chicken_inp, cow_inp, sheep_inp):
    total_legs = chicken_inp * 2 + cow_inp * 4 + sheep_inp * 4
    return total_legs

animals_order = []
chicken_inp = int(input('How many chickens do you have? '))
animals_order.append(chicken_inp)
cow_inp = int(input('How many cows do you have? '))
animals_order.append(cow_inp)
sheep_inp = int(input('How many sheeps do you have? '))
animals_order.append(sheep_inp)

print('Number of your animals in sequencely: ',animals_order,'|| Total number of your animals\' legs: ',
      animals(chicken_inp, cow_inp, sheep_inp))