###
# Kwota w monetach 5, 2 i 1 zł - jak najmniejszą liczbą monet.
#
amount = int(input('Enter the amount in PLN: '))             # wczytujemy kwotę (liczba naturalna)
coins_5 = amount // 5                                        # ile pełnych piątek się mieści
rest = amount % 5                                            # reszta po piątkach
coins_2 = rest // 2                                          # ile dwójek mieści się w reszcie
coins_1 = rest % 2                                           # to, co zostało, płacimy złotówkami
print(f'The amount of PLN {amount} in coins:')               # nagłówek
print(f'5 PLN coins: {coins_5}')                             # liczba monet 5 zł
print(f'2 PLN coins: {coins_2}')                             # liczba monet 2 zł
print(f'1 PLN coins: {coins_1}')                             # liczba monet 1 zł
