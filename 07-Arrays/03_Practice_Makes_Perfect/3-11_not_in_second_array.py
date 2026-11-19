###
# Prints the numbers from the first array that do not appear in the second array
#
first = [4, 36, 12, 28, 9, 44, 5]   # pierwsza lista
second = [5, 1, 36]                 # druga lista

for number in first:                # bierzemy po kolei każdą liczbę z pierwszej listy
    if number not in second:        # not in sprawdza, czy liczby nie ma w drugiej liście
        print(number, end=' ')      # jeśli jej nie ma, wypisujemy ją
print()                             # nowa linia (wynik: 4 12 28 9 44)
