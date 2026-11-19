###
# Returns the number of negative even numbers in the range <x, y>
#
def f(x, y):                                 # funkcja liczy ujemne liczby parzyste od x do y
    counter = 0                              # licznik, na początku 0
    for number in range(x, y + 1):           # bierzemy liczby od x do y (y + 1, bo range nie bierze ostatniej)
        if number < 0 and number % 2 == 0:   # jeśli liczba jest ujemna i parzysta
            counter = counter + 1            # zwiększamy licznik o 1
    return counter                           # funkcja oddaje wynik

def main():                                  # program główny
    print('f(-7, 8) returns', f(-7, 8))      # powinno wyjść 3 (-6, -4, -2)
    print('f(-1, 11) returns', f(-1, 11))    # powinno wyjść 0

if __name__ == "__main__":                   # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                   # wtedy uruchamiamy program główny
