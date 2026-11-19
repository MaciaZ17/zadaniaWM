###
# Checks if the given string of digits is a valid binary number
#
def f(binary_number):                                   # funkcja sprawdza, czy napis to liczba dwójkowa (same 0 i 1)
    if binary_number == '':                             # jeśli napis jest pusty
        return False                                    # to nie jest liczba
    for char in binary_number:                          # pętla: bierzemy po kolei każdy znak
        if char != '0' and char != '1':                 # jeśli znak nie jest ani 0, ani 1
            return False                                # oddajemy False; return od razu kończy funkcję
    return True                                         # wszystkie znaki były dobre, więc oddajemy True

def main():                                             # program główny
    print('f("101101") returns', f("101101"))           # sprawdzamy funkcję, powinno wyjść True
    print('f("1311a10100") returns', f("1311a10100"))   # powinno wyjść False

if __name__ == "__main__":                              # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                              # wtedy uruchamiamy program główny
