###
# Converts a two-dimensional (2D) array into a one-dimensional (1D) array
#
def to_1d(arr):                                        # funkcja zamienia listę list na jedną listę
    result = []                                        # pusta lista na wynik
    for row in arr:                                    # bierzemy po kolei każdy wiersz
        for value in row:                              # bierzemy po kolei każdą wartość
            result.append(value)                       # dopisujemy ją na koniec wyniku
    return result                                      # funkcja oddaje jedną listę

def main():                                            # program główny
    print(to_1d([[2, 3], [1, 5]]))                     # wynik: [2, 3, 1, 5]
    print(to_1d([[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]))   # wynik: [5, 0, 3, 7, 5, 9, 0, 9, 1, 2]
    print(to_1d([[2, 1], [3, 5], [7, 4], [2, 6]]))     # wynik: [2, 1, 3, 5, 7, 4, 2, 6]

if __name__ == "__main__":                             # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                             # wtedy uruchamiamy program główny
