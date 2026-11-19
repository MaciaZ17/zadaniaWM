###
# Sorts arrays using the Bubble Sort algorithm
#
def bubblesort(array):                          # funkcja sortuje listę od najmniejszej do największej
    n = len(array)                              # n to liczba elementów
    for i in range(n):                          # robimy n przejść po liście
        for j in range(n - i - 1):              # porównujemy sąsiednie pary; posortowanej końcówki nie sprawdzamy
            if array[j] > array[j + 1]:         # jeśli element jest większy od następnego
                temp = array[j]                 # zamiana miejscami: zapamiętujemy pierwszy
                array[j] = array[j + 1]         # na jego miejsce wstawiamy drugi
                array[j + 1] = temp             # na miejsce drugiego wstawiamy zapamiętany
    return array                                # funkcja oddaje posortowaną listę

def main():                                     # program główny
    print(bubblesort([5, 1, 4, 2, 8]))          # sortujemy i wypisujemy pierwszą listę
    print(bubblesort([10, -3, 7, 0, -8]))       # drugą listę
    print(bubblesort([99, 15, 42, 1, 73, 8]))   # trzecią listę

if __name__ == "__main__":                      # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                      # wtedy uruchamiamy program główny
