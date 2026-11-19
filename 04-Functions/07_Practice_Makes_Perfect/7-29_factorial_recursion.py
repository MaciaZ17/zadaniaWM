###
# Calculates the factorial recursively
# (in the instructions the second "if" had wrong indentation -
#  it must be inside the function)
#
# Rekurencja: funkcja wywołuje samą siebie, za każdym razem dla mniejszej liczby.
def factorial(n):                     # funkcja liczy silnię, np. 5! = 5 * 4 * 3 * 2 * 1
    if n == 0 or n == 1:              # jeśli n to 0 albo 1
        return 1                      # silnia wynosi 1; tu rekurencja się zatrzymuje
    if n > 1:                         # jeśli n jest większe od 1
        return n * factorial(n - 1)   # n! = n * (n-1)!, funkcja woła samą siebie dla n - 1

# Jak to działa dla n = 5:
# factorial(5) = 5 * factorial(4)
#              = 5 * 4 * factorial(3)
#              = 5 * 4 * 3 * factorial(2)
#              = 5 * 4 * 3 * 2 * factorial(1)
#              = 5 * 4 * 3 * 2 * 1 = 120

def main():                           # program główny
    n = 5                             # liczba, dla której liczymy silnię
    print(f'{n}! =', factorial(n))    # wypisujemy wynik (120)

if __name__ == "__main__":            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                            # wtedy uruchamiamy program główny
