###
# Swaps the first and the last column of a 3 by 5 array
#
def print_2d(arr):                         # funkcja wypisuje listę w wierszach i kolumnach
    for row in arr:                        # bierzemy po kolei każdy wiersz
        for value in row:                  # bierzemy po kolei każdą wartość
            print(f'{value:3}', end=' ')   # :3 zajmuje 3 miejsca, kolumny są równe
        print()                            # nowa linia po wierszu

def main():                                # program główny
    arr = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]                                      # lista 3 na 5
    print('Before:')                       # podpis
    print_2d(arr)                          # wypisujemy przed zmianą

    for row in arr:                        # w każdym wierszu zamieniamy pierwszą i ostatnią liczbę
        last = len(row) - 1                # indeks ostatniej kolumny
        temp = row[0]                      # zapamiętujemy pierwszą liczbę
        row[0] = row[last]                 # na jej miejsce wstawiamy ostatnią
        row[last] = temp                   # na miejsce ostatniej wstawiamy zapamiętaną

    print('After:')                        # podpis
    print_2d(arr)                          # wypisujemy po zmianie

if __name__ == "__main__":                 # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                 # wtedy uruchamiamy program główny
