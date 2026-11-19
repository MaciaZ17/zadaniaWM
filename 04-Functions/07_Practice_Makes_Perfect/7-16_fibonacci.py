###
# Returns the n-th value of the Fibonacci sequence
# (1st value = 0, 2nd value = 1)
#
# Ciąg: 0, 1, 1, 2, 3, 5, 8, 13, 21... (każda liczba to suma dwóch poprzednich)
def f(n):                                 # funkcja oddaje n-tą liczbę ciągu Fibonacciego
    if n == 1:                            # jeśli chodzi o pierwszą liczbę
        return 0                          # to jest 0
    previous = 0                          # pierwsza liczba ciągu
    current = 1                           # druga liczba ciągu
    for i in range(n - 2):                # powtarzamy n - 2 razy, bo dwie pierwsze liczby już mamy
        next_value = previous + current   # następna liczba to suma dwóch poprzednich
        previous = current                # przesuwamy się o jedną liczbę do przodu
        current = next_value              # nowa liczba staje się bieżącą
    return current                        # funkcja oddaje n-tą liczbę

def main():                               # program główny
    print('f(5) returns', f(5))           # powinno wyjść 3
    print('f(9) returns', f(9))           # powinno wyjść 21

if __name__ == "__main__":                # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                # wtedy uruchamiamy program główny
