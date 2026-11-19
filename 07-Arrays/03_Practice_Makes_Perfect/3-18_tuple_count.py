###
# Counts the number of occurrences of a value in a tuple
#
numbers = (50, 20, 40, 50, 30, 50)       # krotka z liczbami

print('Tuple:', end=' ')                 # tekst bez przechodzenia do nowej linii
for i in range(len(numbers)):            # i to kolejne indeksy
    if i > 0:                            # jeśli to nie pierwsza liczba
        print(',', end='')               # wypisujemy przecinek
    print(numbers[i], end='')            # wypisujemy liczbę
print()                                  # nowa linia

value = int(input('Value: '))            # wczytujemy liczbę, której szukamy
count = 0                                # licznik wystąpień, na początku 0
for number in numbers:                   # bierzemy po kolei każdą liczbę
    if number == value:                  # jeśli to szukana liczba
        count = count + 1                # zwiększamy licznik
print('Number of occurrences:', count)   # wypisujemy wynik (dla 50: 3)
