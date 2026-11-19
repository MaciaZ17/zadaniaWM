###
# Prints the array values graphically using asterisks
#
def star(n):                               # funkcja zwraca napis z n gwiazdek
    result = ''                            # pusty napis na start
    for i in range(n):                     # powtarzamy n razy
        result = result + '*'              # doklejamy gwiazdkę
    return result                          # funkcja oddaje napis z gwiazdkami

def main():                                # program główny
    arr = [2, 6, 4, 9, 7]                  # lista liczb
    for value in arr:                      # bierzemy po kolei każdą liczbę
        print(f'{value}: {star(value)}')   # wypisujemy liczbę i tyle gwiazdek, ile wynosi, np. 2: **

if __name__ == "__main__":                 # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                 # wtedy uruchamiamy program główny
