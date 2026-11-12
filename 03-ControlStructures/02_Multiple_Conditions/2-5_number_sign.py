###
# Checks what number was entered from the keyboard.
# Testy: 7, 1, 0, -1, -4
#
number = int(input('Enter number: '))                        # wczytujemy liczbę całkowitą

if number > 0:                                               # liczba większa od zera
    print(f'Number {number} is positive')                    # dodatnia
elif number < 0:                                             # liczba mniejsza od zera
    print(f'Number {number} is negative')                    # ujemna
else:                                                        # jedyna pozostała możliwość: zero
    print('Number is 0')                                     # zero
