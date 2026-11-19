###
# Module with functions to operate on an array of numbers
# (without built-in functions like max, min, sorted, sum)
#
def largest_value(arr):                                            # funkcja pomocnicza: zwraca największą liczbę
    largest = arr[0]                                               # na początku zakładamy, że pierwsza jest największa
    for value in arr:                                              # bierzemy po kolei każdą liczbę
        if value > largest:                                        # jeśli jest większa
            largest = value                                        # zapamiętujemy ją
    return largest                                                 # funkcja oddaje największą

def smallest_value(arr):                                           # funkcja pomocnicza: zwraca najmniejszą liczbę
    smallest = arr[0]                                              # na początku zakładamy, że pierwsza jest najmniejsza
    for value in arr:                                              # bierzemy po kolei każdą liczbę
        if value < smallest:                                       # jeśli jest mniejsza
            smallest = value                                       # zapamiętujemy ją
    return smallest                                                # funkcja oddaje najmniejszą

def sort_numbers(arr):                                             # funkcja pomocnicza: zwraca posortowaną kopię listy (sortowanie bąbelkowe)
    copy = []                                                      # pusta lista na kopię, żeby nie zmieniać oryginału
    for value in arr:                                              # bierzemy po kolei każdą liczbę
        copy.append(value)                                         # dopisujemy ją do kopii
    n = len(copy)                                                  # liczba elementów
    for i in range(n):                                             # robimy n przejść po liście
        for j in range(n - i - 1):                                 # porównujemy sąsiednie pary
            if copy[j] > copy[j + 1]:                              # jeśli są w złej kolejności
                temp = copy[j]                                     # zamieniamy je miejscami
                copy[j] = copy[j + 1]                              # na jego miejsce wstawiamy drugi
                copy[j + 1] = temp                                 # na miejsce drugiego wstawiamy zapamiętany
    return copy                                                    # funkcja oddaje posortowaną kopię

def second_largest(arr):                                           # funkcja zwraca drugą największą liczbę
    largest = largest_value(arr)                                   # największa liczba
    second = smallest_value(arr)                                   # na początku zakładamy, że druga to najmniejsza
    for value in arr:                                              # bierzemy po kolei każdą liczbę
        if value > second and value < largest:                     # jeśli jest większa od zapamiętanej, ale mniejsza od największej
            second = value                                         # zapamiętujemy ją
    return second                                                  # funkcja oddaje drugą największą

def difference(arr):                                               # funkcja zwraca różnicę między największą a najmniejszą liczbą
    return largest_value(arr) - smallest_value(arr)                # największa minus najmniejsza

def median(arr):                                                   # funkcja zwraca medianę, czyli środkową liczbę po posortowaniu
    sorted_arr = sort_numbers(arr)                                 # sortujemy liczby
    n = len(sorted_arr)                                            # liczba elementów
    middle = n // 2                                                # indeks środka
    if n % 2 == 1:                                                 # jeśli liczb jest nieparzyście wiele
        return sorted_arr[middle]                                  # mediana to środkowa liczba
    else:                                                          # jeśli liczb jest parzyście wiele, są dwie środkowe
        return (sorted_arr[middle - 1] + sorted_arr[middle]) / 2   # mediana to ich średnia

def min_max(arr):                                                  # funkcja zwraca listę dwóch liczb: najmniejszej i największej
    return [smallest_value(arr), largest_value(arr)]               # tworzymy listę z dwóch wyników

def to_string(arr):                                                # funkcja zwraca liczby jako napis oddzielony minusami
    result = ''                                                    # pusty napis na start
    for i in range(len(arr)):                                      # i to kolejne indeksy
        if i > 0:                                                  # jeśli to nie pierwsza liczba
            result = result + '-'                                  # doklejamy minus
        result = result + str(arr[i])                              # doklejamy liczbę zamienioną na napis
    return result                                                  # funkcja oddaje napis
