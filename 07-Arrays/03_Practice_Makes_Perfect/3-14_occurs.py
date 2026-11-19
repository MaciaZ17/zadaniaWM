###
# Checks whether the number entered from the keyboard is present in the array
#
def occurs(number, array):                                            # funkcja sprawdza, czy liczba jest w liście
    for value in array:                                               # bierzemy po kolei każdy element
        if value == number:                                           # jeśli to szukana liczba
            return True                                               # znaleźliśmy ją, oddajemy True
    return False                                                      # przeszliśmy całą listę i jej nie ma

def main():                                                           # program główny
    array = [15, 38, 7, 23, 14]                                       # lista liczb
    number = int(input('Number: '))                                   # wczytujemy liczbę z klawiatury
    print('Array:', end=' ')                                          # tekst bez przechodzenia do nowej linii
    for value in array:                                               # bierzemy po kolei każdy element
        print(value, end=' ')                                         # wypisujemy go ze spacją
    print()                                                           # nowa linia
    if occurs(number, array):                                         # jeśli liczba jest w liście
        print('Result: number', number, 'appears in the array')       # wypisujemy, że jest
    else:                                                             # w przeciwnym razie
        print('Result: number', number, 'does not appear in the array')  # wypisujemy, że jej nie ma

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
