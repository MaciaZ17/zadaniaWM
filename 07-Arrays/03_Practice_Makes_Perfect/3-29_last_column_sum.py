###
# Calculates the sum of values in the last column
#
arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]                                         # lista dwuwymiarowa: 4 wiersze po 5 liczb

total = 0                                 # suma, na początku 0
for row in arr:                           # bierzemy po kolei każdy wiersz
    total = total + row[len(row) - 1]     # dodajemy ostatnią liczbę z wiersza
print('Sum of the last column:', total)   # wypisujemy wynik (0 + 5 + 7 + 5 = 17)
