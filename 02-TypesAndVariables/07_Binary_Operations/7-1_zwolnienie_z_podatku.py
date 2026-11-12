###
# Zwolnienie z podatku do 26 roku życia włącznie.
# Testy: 38 -> False, 27 -> False, 26 -> True, 22 -> True, 18 -> True
#
age = int(input('Enter age: '))                    # wczytujemy wiek jako liczbę całkowitą
no_tax = age <= 26                                 # porównanie daje True/False (<= bo 26 lat też jest zwolnione)
print(f'Exemption from paying taxes: {no_tax}')    # wypisujemy wynik
