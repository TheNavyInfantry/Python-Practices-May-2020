# numbers = [1, 2, 3, 4, 5]

numbers = [1, 2]

indices = []

for each in numbers:
    index = numbers.index(each)
    indices.append(index)

print(indices)







# Her elemanın kendi indeksi ile çarpıldığı listede tüm elemanların toplamını döndürün. Boş listeler için 0 döndürün.
#
# Örnekler
#
# index_carpici([1, 2, 3, 4, 5]) ➞ 40
# # (1*0 + 2*1 + 3*2 + 4*3 + 5*4)
#
# index_carpici([-3, 0, 8, -6]) ➞ -2
# # (-3*0 + 0*1 + 8*2 + -6*3)