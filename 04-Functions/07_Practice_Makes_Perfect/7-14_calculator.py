###
# Returns the result of an arithmetic operation
# (available operators: + - * % **)
#
def f(number1, number2, operator):                  # funkcja liczy wynik działania; operator to znak działania
    if operator == '+':                             # jeśli znak to +
        return number1 + number2                    # dodajemy
    elif operator == '-':                           # jeśli znak to -
        return number1 - number2                    # odejmujemy
    elif operator == '*':                           # jeśli znak to *
        return number1 * number2                    # mnożymy
    elif operator == '%':                           # jeśli znak to %
        return number1 % number2                    # reszta z dzielenia (2 % 3 = 2)
    elif operator == '**':                          # jeśli znak to **
        return number1 ** number2                   # potęgowanie (2 ** 3 = 8)
    else:                                           # jeśli znak jest inny
        return None                                 # None znaczy "brak wyniku"

def main():                                         # program główny
    print('f(2, 3, "+") returns', f(2, 3, "+"))     # powinno wyjść 5
    print('f(2, 3, "%") returns', f(2, 3, "%"))     # powinno wyjść 2
    print('f(2, 3, "**") returns', f(2, 3, "**"))   # powinno wyjść 8
    print('f(2, 3, "*") returns', f(2, 3, "*"))     # powinno wyjść 6
    print('f(2, 3, "-") returns', f(2, 3, "-"))     # powinno wyjść -1

if __name__ == "__main__":                          # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                          # wtedy uruchamiamy program główny
