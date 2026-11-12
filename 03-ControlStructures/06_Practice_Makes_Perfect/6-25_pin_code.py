###
# Sprawdzanie PIN-u 0805, maksymalnie 3 próby.
# PIN wczytujemy jako TEKST - gdyby był liczbą, zero z przodu by zniknęło (0805 -> 805).
#
correct_pin = '0805'                                         # poprawny PIN
attempts = 0                                                 # liczba wykonanych prób
pin_ok = False                                               # czy PIN został podany poprawnie

while attempts < 3 and not pin_ok:                           # działamy, dopóki są próby i PIN jeszcze nie był poprawny
    entered_pin = input('Enter the PIN code: ')              # wczytujemy PIN
    attempts += 1                                            # liczymy próbę
    if entered_pin == correct_pin:                           # PIN poprawny
        pin_ok = True                                        # zapamiętujemy sukces (pętla się zakończy)
        print('PIN code correct')                            # komunikat
    else:                                                    # PIN błędny
        print('Incorrect...')                                # komunikat

if not pin_ok:                                               # po pętli: jeśli nadal brak sukcesu, to były 3 błędne próby
    print('Sorry, your payment card has been blocked.')      # blokada karty
