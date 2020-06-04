vowels = 'aeiouAEIOU'
vowel_list = []
for v in vowels:
    vowel_list.append(v)
print(vowel_list)

user_input = str(input('Type: '))
empty_list = []

for each in user_input:
    empty_list.append(each)
    if empty_list in vowel_list:
        empty_list.remove(vowel_list)
print(empty_list)


# Bir string alan ve tüm sesli harflerin çıkarıldığı yeni bir string döndüren bir fonksiyon oluşturun.
#
# Örnekler
#
# sesli_kaldir("Hayatımda hiç Diyet Kola içen ince bir insan görmedim.")
# ➞ " Hytmd hç Dyt Kl çn nc br nsn grmdm.”
#
# sesli_kaldir("Duvar inşa edeceğiz!")
# ➞ "Dvr nş dcğz!"
#
