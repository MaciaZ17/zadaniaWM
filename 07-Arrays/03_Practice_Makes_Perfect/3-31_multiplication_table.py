###
# Modifies the array values to create a multiplication table
#
table = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]                                         # tablica 5 na 5 z zerami (w treści brakuje jednego nawiasu, tu jest poprawiona)

for i in range(len(table)):               # i to numer wiersza: 0, 1, ... 4
    for j in range(len(table[i])):        # j to numer kolumny: 0, 1, ... 4
        table[i][j] = (i + 1) * (j + 1)   # dodajemy 1, bo tabliczka zaczyna się od 1, a indeksy od 0

for row in table:                         # bierzemy po kolei każdy wiersz
    for value in row:                     # bierzemy po kolei każdą wartość
        print(f'{value:2}', end=' ')      # :2 zajmuje 2 miejsca, dzięki temu kolumny są równe
    print()                               # nowa linia po wierszu
