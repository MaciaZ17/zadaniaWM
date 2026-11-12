###
# Kupon lotto 1..49: 7 wierszy po 7 liczb; kolejne liczby w kolumnach.
# W wierszu r (1..7) i kolumnie c (0..6) stoi liczba r + 7*c.
#
for row in range(1, 8):                                      # wiersze od 1 do 7
    for column in range(7):                                  # kolumny 0..6
        number = row + 7 * column                            # liczba w tym miejscu kuponu
        print(f'{number:2}', end=' ')                        # :2 - szerokość 2 znaki, żeby kolumny były równe
    print()                                                  # po wierszu nowa linia
