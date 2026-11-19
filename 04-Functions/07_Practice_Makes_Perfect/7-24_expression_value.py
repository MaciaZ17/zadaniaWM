###
# Returns the value of an expression with adding and
# subtracting single-digit numbers, e.g. "2+3-4"
#
# Znaki w napisie "2+3-4" mają numery: 0='2', 1='+', 2='3', 3='-', 4='4'.
def f(expression):                                    # funkcja liczy wynik działania zapisanego jako napis
    result = int(expression[0])                       # zaczynamy od pierwszej cyfry
    for i in range(1, len(expression), 2):            # i = 1, 3, 5... czyli miejsca, gdzie stoją znaki + i -
        operator = expression[i]                      # bierzemy znak działania
        digit = int(expression[i + 1])                # bierzemy cyfrę, która stoi za znakiem
        if operator == '+':                           # jeśli to plus
            result = result + digit                   # dodajemy cyfrę
        elif operator == '-':                         # jeśli to minus
            result = result - digit                   # odejmujemy cyfrę
    return result                                     # funkcja oddaje wynik

def main():                                           # program główny
    print('f("2+3") returns', f("2+3"))               # powinno wyjść 5
    print('f("3+8+1") returns', f("3+8+1"))           # powinno wyjść 12
    print('f("2+3-4+5-0") returns', f("2+3-4+5-0"))   # powinno wyjść 6

if __name__ == "__main__":                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                            # wtedy uruchamiamy program główny
