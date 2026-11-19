###
# Checks whether the first array is a subset of the second one
#
def is_subset(first, second):                          # funkcja sprawdza, czy każdy element pierwszej listy jest w drugiej
    for value in first:                                # bierzemy po kolei każdy element pierwszej listy
        if value not in second:                        # jeśli nie ma go w drugiej liście
            return False                               # to nie jest podzbiór
    return True                                        # wszystkie elementy się znalazły, więc to podzbiór

def main():                                            # program główny
    print(is_subset([2, 5, 8], [1, 2, 3, 5, 8, 13]))   # powinno wyjść True
    print(is_subset([2, 4], [1, 2, 3, 5, 8, 13]))      # powinno wyjść False (brak 4)

if __name__ == "__main__":                             # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                             # wtedy uruchamiamy program główny
