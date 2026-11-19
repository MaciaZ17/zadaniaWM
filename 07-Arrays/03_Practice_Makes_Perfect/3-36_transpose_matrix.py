###
# Transposes matrices (rows become columns)
#
def transpose_matrix(m):                      # funkcja zamienia wiersze na kolumny
    rows = len(m)                             # liczba wierszy
    cols = len(m[0])                          # liczba kolumn (długość pierwszego wiersza)
    result = []                               # pusta lista na nową macierz
    for j in range(cols):                     # każda kolumna stanie się nowym wierszem
        new_row = []                          # nowy, pusty wiersz
        for i in range(rows):                 # przechodzimy w dół kolumny
            new_row.append(m[i][j])           # dopisujemy liczbę z wiersza i, kolumny j
        result.append(new_row)                # dopisujemy gotowy wiersz
    return result                             # funkcja oddaje nową macierz

def print_matrix(matrix):                     # funkcja wypisuje macierz w wierszach i kolumnach
    for row in matrix:                        # bierzemy po kolei każdy wiersz
        for value in row:                     # bierzemy po kolei każdą wartość
            print(value, end=' ')             # wypisujemy ją ze spacją
        print()                               # nowa linia po wierszu

def main():                                   # program główny
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]    # macierz 3 na 3
    m2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]   # macierz 2 na 5
    m3 = [[5, 6, 7, 8]]                       # macierz 1 na 4
    for m in [m1, m2, m3]:                    # bierzemy po kolei każdą macierz
        print_matrix(transpose_matrix(m))     # transponujemy i wypisujemy
        print()                               # pusta linia między macierzami

if __name__ == "__main__":                    # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                    # wtedy uruchamiamy program główny
