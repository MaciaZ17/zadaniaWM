###
# EAN-13: dokładnie 13 cyfr; kod zaczynający się od 590 oznacza Polskę.
#
ean = input('Enter EAN-13 article number: ')                 # wczytujemy numer jako TEKST (liczba mogłaby zgubić zera)
if len(ean) == 13 and ean.isdigit():                         # dokładnie 13 znaków i wszystkie są cyframi
    print('Article number is correct')                       # numer poprawny
    if ean[0:3] == '590':                                    # to sprawdzamy tylko dla poprawnego numeru (zagnieżdżony if)
        print('Article manufactured in Poland')              # produkt z Polski
else:                                                        # numer niepoprawny
    print('Article number is incorrect')                     # komunikat
