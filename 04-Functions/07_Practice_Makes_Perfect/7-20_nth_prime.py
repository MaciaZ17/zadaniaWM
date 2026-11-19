###
# Returns the n-th prime number
#
def is_prime(number):                  # funkcja pomocnicza: sprawdza, czy liczba jest pierwsza
    if number < 2:                     # jeśli liczba jest mniejsza od 2
        return False                   # to nie jest pierwsza
    for divisor in range(2, number):   # sprawdzamy dzielniki od 2 do liczby mniejszej o 1
        if number % divisor == 0:      # jeśli dzieli się bez reszty
            return False               # to nie jest pierwsza
    return True                        # nie znaleźliśmy dzielnika, więc jest pierwsza

def f(n):                              # funkcja szuka n-tej liczby pierwszej
    found = 0                          # ile liczb pierwszych już znaleźliśmy
    number = 1                         # liczba, którą sprawdzamy
    while found < n:                   # szukamy, dopóki nie znajdziemy n liczb pierwszych
        number = number + 1            # bierzemy następną liczbę
        if is_prime(number):           # jeśli jest pierwsza
            found = found + 1          # zwiększamy licznik znalezionych
    return number                      # ostatnia znaleziona to n-ta liczba pierwsza

def main():                            # program główny
    print('f(1) returns', f(1))        # powinno wyjść 2
    print('f(5) returns', f(5))        # powinno wyjść 11 (2, 3, 5, 7, 11)

if __name__ == "__main__":             # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                             # wtedy uruchamiamy program główny
