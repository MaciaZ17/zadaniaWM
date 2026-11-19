###
# Computes the sum of the even digits (even = True)
# or the odd digits (even = False) of a number
#
def f(number, even):                                    # funkcja sumuje cyfry parzyste (even=True) albo nieparzyste (even=False)
    total = 0                                           # suma, na początku 0
    for char in str(abs(number)):                       # usuwamy minus, zamieniamy na napis i bierzemy po kolei każdą cyfrę
        digit = int(char)                               # zamieniamy cyfrę z napisu na liczbę
        if even == True and digit % 2 == 0:             # jeśli szukamy parzystych i cyfra jest parzysta (dzieli się przez 2)
            total = total + digit                       # dodajemy ją do sumy
        elif even == False and digit % 2 == 1:          # jeśli szukamy nieparzystych i cyfra jest nieparzysta
            total = total + digit                       # dodajemy ją do sumy
    return total                                        # funkcja oddaje sumę

def main():                                             # program główny
    print('f(3124, True) returns', f(3124, True))       # powinno wyjść 6 (2 + 4)
    print('f(3124, False) returns', f(3124, False))     # powinno wyjść 4 (3 + 1)
    print('f(20576, False) returns', f(20576, False))   # powinno wyjść 12 (5 + 7)
    print('f(20576, True) returns', f(20576, True))     # powinno wyjść 8 (2 + 0 + 6)
    print('f(13115, True) returns', f(13115, True))     # powinno wyjść 0 (brak parzystych)

if __name__ == "__main__":                              # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                              # wtedy uruchamiamy program główny
