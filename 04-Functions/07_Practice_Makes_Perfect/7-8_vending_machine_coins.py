###
# Returns the minimum number of coins (1, 2 and 5 PLN)
# needed to pay the given amount
#
# Najmniej monet wychodzi, gdy płacimy najpierw największymi.
def f(amount_to_pay):                    # funkcja liczy, ile monet trzeba, żeby zapłacić kwotę
    coins_5 = amount_to_pay // 5         # // dzieli bez reszty: ile monet 5 zł się mieści (23 // 5 = 4)
    rest = amount_to_pay % 5             # % daje resztę z dzielenia: ile zostało do zapłaty (23 % 5 = 3)
    coins_2 = rest // 2                  # ile monet 2 zł mieści się w reszcie
    rest = rest % 2                      # co zostało po monetach 2 zł (0 albo 1)
    coins_1 = rest                       # resztę płacimy monetami 1 zł
    return coins_5 + coins_2 + coins_1   # funkcja oddaje liczbę wszystkich monet

def main():                              # program główny
    print('f(23) returns', f(23))        # powinno wyjść 6
    print('f(8) returns', f(8))          # powinno wyjść 3
    print('f(2) returns', f(2))          # powinno wyjść 1
    print('f(0) returns', f(0))          # powinno wyjść 0

if __name__ == "__main__":               # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                               # wtedy uruchamiamy program główny
