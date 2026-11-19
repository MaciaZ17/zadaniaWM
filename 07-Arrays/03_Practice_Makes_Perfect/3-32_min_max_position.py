###
# Finds the smallest and largest values and their row and column
#
arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]                        # lista dwuwymiarowa: 4 wiersze po 2 liczby

min_value = arr[0][0]                                                 # na początku zakładamy, że pierwsza liczba jest najmniejsza
min_row = 0                                                           # i zapamiętujemy jej wiersz
min_col = 0                                                           # i kolumnę
max_value = arr[0][0]                                                 # tak samo dla największej
max_row = 0                                                           # jej wiersz
max_col = 0                                                           # i kolumnę

for i in range(len(arr)):                                             # i to numer wiersza
    for j in range(len(arr[i])):                                      # j to numer kolumny
        if arr[i][j] < min_value:                                     # jeśli liczba jest mniejsza od dotychczas najmniejszej
            min_value = arr[i][j]                                     # zapamiętujemy ją
            min_row = i                                               # i jej wiersz
            min_col = j                                               # i kolumnę
        if arr[i][j] > max_value:                                     # jeśli jest większa od dotychczas największej
            max_value = arr[i][j]                                     # zapamiętujemy ją
            max_row = i                                               # i jej wiersz
            max_col = j                                               # i kolumnę

# Do numerów dodajemy 1, bo ludzie liczą od 1, a Python od 0.
print('Smallest value:', min_value, 'row', min_row + 1, 'column', min_col + 1)  # -38, wiersz 1, kolumna 1
print('Largest value:', max_value, 'row', max_row + 1, 'column', max_col + 1)  # 40, wiersz 2, kolumna 2
