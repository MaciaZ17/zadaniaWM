###
# Replaces the values of the main diagonal with 1
#
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]                               # macierz 3x3 z samymi zerami

# Główna przekątna to pola, gdzie numer wiersza = numer kolumny: [0][0], [1][1], [2][2].
for i in range(len(matrix)):    # i to kolejne numery: 0, 1, 2
    matrix[i][i] = 1            # wstawiamy 1 w wierszu i, kolumnie i

for row in matrix:              # bierzemy po kolei każdy wiersz
    for value in row:           # bierzemy po kolei każdą wartość w wierszu
        print(value, end=' ')   # wypisujemy ją ze spacją
    print()                     # po wierszu przechodzimy do nowej linii
