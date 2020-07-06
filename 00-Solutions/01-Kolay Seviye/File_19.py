inp = input(">> ")
inp = inp.split()
new_Sentence = []
hyphen_Counter = 0

for element in inp:
    if len(element) > 2:
        hyphen_Counter = len(element)-2

    else:
        hyphen_Counter = 0
    new_Sentence.append(element[0]+"-"*hyphen_Counter+element[-1])

conclusion = ' '.join(new_Sentence)
print(conclusion)


