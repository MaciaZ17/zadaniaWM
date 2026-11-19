###
# Calculates the sum of natural numbers from 1 to n
# using recursion
#
def sum_natural(n):                                                   # funkcja liczy sumę 1 + 2 + ... + n
    if n == 1:                                                        # jeśli n to 1
        return 1                                                      # suma to 1; tu rekurencja się zatrzymuje
    return n + sum_natural(n - 1)                                     # dodajemy n do sumy liczb od 1 do n - 1

def main():                                                           # program główny
    print('The sum of natural numbers in the range <1,10> is', sum_natural(10))  # wypisujemy wynik (55)

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
