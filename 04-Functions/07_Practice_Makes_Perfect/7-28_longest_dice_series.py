###
# Returns the number on the dice that was rolled
# the most times in a row
#
def f(dice):                                                  # funkcja szuka liczby oczek, która wypadła najwięcej razy pod rząd
    best_digit = dice[0]                                      # najlepsza seria na razie: pierwszy rzut
    best_length = 1                                           # długość najlepszej serii
    current_length = 1                                        # długość serii, która trwa teraz
    for i in range(1, len(dice)):                             # bierzemy rzuty od drugiego do ostatniego
        if dice[i] == dice[i - 1]:                            # jeśli wypadło to samo co w poprzednim rzucie
            current_length = current_length + 1               # seria rośnie o 1
        else:                                                 # jeśli wypadło coś innego
            current_length = 1                                # zaczyna się nowa seria
        if current_length > best_length:                      # jeśli obecna seria jest dłuższa niż najlepsza
            best_length = current_length                      # zapamiętujemy jej długość
            best_digit = dice[i]                              # i liczbę oczek
    return int(best_digit)                                    # funkcja oddaje liczbę oczek

def main():                                                   # program główny
    print('f("5233165554211") returns', f("5233165554211"))   # powinno wyjść 5 (555)
    print('f("2133") returns', f("2133"))                     # powinno wyjść 3 (33)

if __name__ == "__main__":                                    # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                    # wtedy uruchamiamy program główny
