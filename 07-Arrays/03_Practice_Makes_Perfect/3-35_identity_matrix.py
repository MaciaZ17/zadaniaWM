###
# Creates and prints identity matrices
#
# Macierz jednostkowa ma jedynki na przekątnej (wiersz = kolumna), a wszędzie indziej zera.
def identity_matrix(n):                       # funkcja tworzy macierz jednostkową n na n
    matrix = []                               # pusta lista na wiersze
    for i in range(n):                        # i to numer wiersza
        row = []                              # nowy, pusty wiersz
        for j in range(n):                    # j to numer kolumny
            if i == j:                        # jeśli to pole na przekątnej
                row.append(1)                 # dopisujemy 1
            else:                             # w przeciwnym razie
                row.append(0)                 # dopisujemy 0
        matrix.append(row)                    # dopisujemy gotowy wiersz do macierzy
    return matrix                             # funkcja oddaje macierz

def print_matrix(matrix):                     # funkcja wypisuje macierz w wierszach i kolumnach
    for row in matrix:                        # bierzemy po kolei każdy wiersz
        for value in row:                     # bierzemy po kolei każdą wartość
            print(value, end=' ')             # wypisujemy ją ze spacją
        print()                               # nowa linia po wierszu

def main():                                   # program główny
    for size in [3, 5, 8]:                    # bierzemy po kolei rozmiary 3, 5 i 8
        print_matrix(identity_matrix(size))   # tworzymy macierz i ją wypisujemy
        print()                               # pusta linia między macierzami

if __name__ == "__main__":                    # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                    # wtedy uruchamiamy program główny
