def simplification(data):
    if type(data) == list:
        return simplification(data[0])
    else:
        return data

data = [[[[[[[[[[[[[[[[['Find this text']]]]]]]]]]]]]]]]]
print(simplification(data))
















# found = False
# for sublist in data:
#
#     if search in sublist:
#         print('Here')
#         found = True
#     else:
#         print('Not here!')
#         print(data)