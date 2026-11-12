###
# Zamiana liczby dziesiętnej na binarną metodą dzielenia przez 2. Przykład: 12 -> 1100
#
decimal = int(input('Enter decimal number: '))              # wczytujemy liczbę
number = decimal                                             # kopia robocza (oryginał potrzebny do wydruku)
binary = ''                                                  # tu zbudujemy wynik jako tekst

if number == 0:                                              # zero trzeba obsłużyć osobno (pętla by się nie wykonała)
    binary = '0'                                             # zero binarnie to 0

while number > 0:                                            # dzielimy, aż iloraz wyniesie 0
    remainder = number % 2                                   # reszta z dzielenia przez 2 (0 albo 1)
    binary = str(remainder) + binary                         # dopisujemy resztę Z PRZODU - dzięki temu czytamy od dołu do góry
    number = number // 2                                     # iloraz całkowity staje się nową liczbą

print(f'{decimal}(10) = {binary}(2)')                        # wypisujemy wynik
