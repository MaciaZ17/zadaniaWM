###
# Returns True if the product code is correct: the 4th digit
# is the remainder of dividing the sum of the first 3 digits by 7
#
def f(product_code):                                                  # funkcja sprawdza, czy kod produktu jest poprawny
    if len(product_code) != 4:                                        # jeśli kod nie ma dokładnie 4 znaków
        return False                                                  # jest zły
    digits_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])  # dodajemy 3 pierwsze cyfry
    control_digit = int(product_code[3])                              # czwarta cyfra to cyfra kontrolna
    return digits_sum % 7 == control_digit                            # True, gdy reszta z dzielenia sumy przez 7 równa się cyfrze kontrolnej

def main():                                                           # program główny
    print('f("1082") returns', f("1082"))                             # powinno wyjść True (1+0+8 = 9, 9 % 7 = 2)
    print('f("2035") returns', f("2035"))                             # powinno wyjść True
    print('f("1114") returns', f("1114"))                             # powinno wyjść False
    print('f("7071") returns', f("7071"))                             # powinno wyjść False

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
