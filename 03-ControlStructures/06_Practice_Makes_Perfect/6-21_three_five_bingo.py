###
# Liczby 1..30: THREE (podzielne przez 3), FIVE (przez 5), BINGO (przez 3 i 5)
# Kolejność warunków ma znaczenie: BINGO sprawdzamy NAJPIERW, inaczej 15 zostałoby tylko THREE.
#
for i in range(1, 31):                                       # liczby od 1 do 30
    if i % 3 == 0 and i % 5 == 0:                            # podzielna przez 3 i przez 5
        print('BINGO', end=' ')                              # end=' ' - kolejne wyniki w jednej linii
    elif i % 3 == 0:                                         # tylko przez 3
        print('THREE', end=' ')                              # THREE
    elif i % 5 == 0:                                         # tylko przez 5
        print('FIVE', end=' ')                               # FIVE
    else:                                                    # żaden z warunków
        print(i, end=' ')                                    # zwykła liczba
print()                                                      # na końcu przechodzimy do nowej linii
