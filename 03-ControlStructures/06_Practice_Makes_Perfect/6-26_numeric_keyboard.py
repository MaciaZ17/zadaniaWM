###
# Klawiatura numeryczna - wersja z pętlami while zamiast for.
# Oryginał:
#   for i in range(6,-1,-3):
#       for j in range(1,4):
#           print(f'{i+j}',end=' ')
#       print()
#
i = 6                                                        # i = numer "startowy" wiersza: 6, 3, 0 (odpowiada range(6,-1,-3))
while i >= 0:                                                # range(6,-1,-3) kończy się przed -1, więc działamy dla i >= 0
    j = 1                                                    # j zaczyna od 1 w każdym wierszu (odpowiada range(1,4))
    while j <= 3:                                            # j = 1, 2, 3
        print(f'{i+j}', end=' ')                             # wypisujemy numer klawisza w tej samej linii
        j += 1                                               # kolejna kolumna
    print()                                                  # po wierszu przechodzimy do nowej linii
    i -= 3                                                   # przechodzimy do niższego wiersza (krok -3)
