###
# Prints a Tic-Tac-Toe board
#
# Lista dwuwymiarowa to lista list: każdy element to cały wiersz.
# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]                               # plansza: 3 wiersze po 3 pola

for row in tic_tac_toe_board:   # pętla: bierzemy po kolei każdy wiersz
    for cell in row:            # druga pętla: bierzemy po kolei każde pole w wierszu
        print(cell, end=" ")    # wypisujemy pole i spację, bez przechodzenia do nowej linii
    print()                     # po całym wierszu przechodzimy do nowej linii
