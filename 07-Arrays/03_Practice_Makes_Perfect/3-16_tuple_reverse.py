###
# Prints the tuple in reverse order
#
numbers = (10, 20, 30, 40, 50)      # krotka z liczbami

text = ''                           # pusty napis, zbudujemy w nim liczby po przecinku
for i in range(len(numbers)):       # i to kolejne indeksy: 0, 1, ... 4
    if i > 0:                       # jeśli to nie pierwsza liczba
        text = text + ','           # doklejamy przecinek
    text = text + str(numbers[i])   # doklejamy liczbę zamienioną na napis
print('Tuple:', text)               # wypisujemy: 10,20,30,40,50

text = ''                           # znowu pusty napis, tym razem od tyłu
i = len(numbers) - 1                # zaczynamy od indeksu ostatniej liczby
while i >= 0:                       # idziemy do tyłu, aż do indeksu 0
    text = text + str(numbers[i])   # doklejamy liczbę
    if i > 0:                       # jeśli to nie ostatnia liczba do wypisania
        text = text + ','           # doklejamy przecinek
    i = i - 1                       # cofamy się o jeden element
print('Reverse order:', text)       # wypisujemy: 50,40,30,20,10
