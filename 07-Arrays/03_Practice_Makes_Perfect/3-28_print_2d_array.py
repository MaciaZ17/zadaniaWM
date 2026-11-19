###
# Prints a 2 by 4 array in rows and columns
#
arr = [
    [4, 8, 15, 16],
    [23, 42, 7, 1]
]                                      # lista dwuwymiarowa: 2 wiersze po 4 liczby

for row in arr:                        # bierzemy po kolei każdy wiersz
    for value in row:                  # bierzemy po kolei każdą liczbę w wierszu
        print(f'{value:3}', end=' ')   # :3 zajmuje 3 miejsca, dzięki temu kolumny są równe
    print()                            # po wierszu przechodzimy do nowej linii
