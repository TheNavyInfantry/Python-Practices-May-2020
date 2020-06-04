def vowel_remover(sentence):
    vowels = 'aeiouAEIOU'
    vowels_list = []
    for element in vowels:
        vowels_list.append(element)
        for char in sentence:
            if char in vowels_list:
                sentence =  sentence.replace(char,'')
    return sentence

sentence = input('Type your sentence: ')
print('New sentence is: ',vowel_remover(sentence))





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
