###
# Compares two arrays: they are the same if they have the same
# number of elements and equal values at the same indexes
#
def compare(array1, array2):                                          # funkcja sprawdza, czy dwie listy są takie same
    if len(array1) != len(array2):                                    # jeśli mają różną liczbę elementów
        return False                                                  # nie są takie same
    for i in range(len(array1)):                                      # i to kolejne indeksy
        if array1[i] != array2[i]:                                    # jeśli elementy o tym samym indeksie się różnią
            return False                                              # listy nie są takie same
    return True                                                       # wszystko się zgadza, więc listy są takie same

def print_array(label, array):                                        # funkcja wypisuje opis i elementy listy oddzielone spacją
    print(label, end=' ')                                             # wypisujemy opis, np. Array1:
    for value in array:                                               # bierzemy po kolei każdy element
        print(value, end=' ')                                         # wypisujemy go ze spacją
    print()                                                           # nowa linia

def show_comparison(array1, array2):                                  # funkcja wypisuje obie listy i wynik porównania
    print_array('Array1:', array1)                                    # wypisujemy pierwszą listę
    print_array('Array2:', array2)                                    # wypisujemy drugą listę
    if compare(array1, array2):                                       # jeśli listy są takie same
        print('Comparison: arrays are the same')                      # wypisujemy, że są takie same
    else:                                                             # w przeciwnym razie
        print('Comparison: arrays are different')                     # wypisujemy, że są różne
    print()                                                           # pusta linia dla czytelności

def main():                                                           # program główny
    show_comparison(["water", "book", "sky"], ["water", "book", "sky"])  # takie same
    show_comparison([True, False], [True, False, True])               # różna liczba elementów
    show_comparison([5, 3, 1], [5, 3, 1])                             # takie same
    show_comparison([3, 2, 1], [3, 2])                                # różna liczba elementów

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
