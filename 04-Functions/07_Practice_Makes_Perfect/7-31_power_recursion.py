###
# Calculates x to the power of n using recursion
#
def power(x, n):                                   # funkcja liczy x do potęgi n
    if n == 0:                                     # jeśli potęga to 0
        return 1                                   # wynik to 1; tu rekurencja się zatrzymuje
    return x * power(x, n - 1)                     # x do potęgi n = x * (x do potęgi n - 1)

def main():                                        # program główny
    print('5 to the power of 3 is', power(5, 3))   # wypisujemy wynik (125)

if __name__ == "__main__":                         # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                         # wtedy uruchamiamy program główny
