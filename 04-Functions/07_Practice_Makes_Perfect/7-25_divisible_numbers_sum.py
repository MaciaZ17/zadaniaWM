###
# Returns the sum of numbers in the range <x, y> that are
# divisible by 2 and 3 and not divisible by 4
#
def f(x, y):                                                          # funkcja sumuje wybrane liczby od x do y
    total = 0                                                         # suma, na początku 0
    for number in range(x, y + 1):                                    # bierzemy liczby od x do y
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:   # dzieli się przez 2 i przez 3, ale nie przez 4
            total = total + number                                    # dodajemy liczbę do sumy
    return total                                                      # funkcja oddaje sumę

def main():                                                           # program główny
    print('f(1, 20) returns', f(1, 20))                               # powinno wyjść 24 (6 + 18)
    print('f(10, 30) returns', f(10, 30))                             # powinno wyjść 48 (18 + 30)

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
