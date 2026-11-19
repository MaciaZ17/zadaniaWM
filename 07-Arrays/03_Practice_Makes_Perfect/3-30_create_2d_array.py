###
# Creates a two-dimensional array filled with zeros
#
def create_2d_arr(x, y):            # funkcja tworzy listę x wierszy po y zer
    arr = []                        # pusta lista na wiersze
    for i in range(x):              # powtarzamy dla każdego wiersza
        row = []                    # nowy, pusty wiersz
        for j in range(y):          # powtarzamy dla każdej kolumny
            row.append(0)           # dopisujemy zero do wiersza
        arr.append(row)             # dopisujemy gotowy wiersz do listy
    return arr                      # funkcja oddaje gotową listę

def main():                         # program główny
    arr = create_2d_arr(3, 5)       # tworzymy listę 3 na 5
    for row in arr:                 # bierzemy po kolei każdy wiersz
        for value in row:           # bierzemy po kolei każdą wartość
            print(value, end=' ')   # wypisujemy ją ze spacją
        print()                     # nowa linia po wierszu

if __name__ == "__main__":          # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                          # wtedy uruchamiamy program główny
