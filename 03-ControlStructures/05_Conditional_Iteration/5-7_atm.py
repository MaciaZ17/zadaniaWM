###
# atm.py - prosty bankomat: wpłata, wypłata, saldo + NOWE: sprawdzenie PIN i zmiana PIN
# UWAGA: nie miałem Twojego oryginalnego atm.py, więc napisałem pełną wersję z menu.
# Jeśli Twój wygląda inaczej, przenieś do niego opcje 4 i 5 (i zmienną pin).
#
balance = 1000.0                                             # początkowe saldo konta
pin = '1234'                                                 # PIN trzymamy jako TEKST (liczba zgubiłaby zera na początku, np. 0805)
choice = ''                                                  # wybór z menu (na start pusty)

while choice != '0':                                         # menu działa, dopóki użytkownik nie wybierze 0
    print('--- ATM ---')                                     # nagłówek menu
    print('1 - Deposit')                                     # opcja wpłaty
    print('2 - Withdraw')                                    # opcja wypłaty
    print('3 - Check balance')                               # opcja salda
    print('4 - Check PIN')                                   # NOWA opcja: sprawdzenie PIN
    print('5 - Change PIN')                                  # NOWA opcja: zmiana PIN
    print('0 - Exit')                                        # wyjście
    choice = input('Choose option: ')                        # wczytujemy wybór użytkownika

    if choice == '1':                                        # wpłata
        amount = float(input('Enter amount to deposit: '))   # wczytujemy kwotę
        if amount > 0:                                       # kwota musi być dodatnia
            balance += amount                                # zwiększamy saldo
            print(f'Deposited {amount:.2f}. Balance: {balance:.2f}')   # potwierdzenie
        else:                                                # kwota <= 0
            print('Amount must be positive')                 # komunikat o błędzie
    elif choice == '2':                                      # wypłata
        amount = float(input('Enter amount to withdraw: '))  # wczytujemy kwotę
        if amount <= 0:                                      # kwota nieprawidłowa
            print('Amount must be positive')                 # komunikat o błędzie
        elif amount > balance:                               # za mało środków
            print('No funds')                                # komunikat o braku środków
        else:                                                # wszystko w porządku
            balance -= amount                                # zmniejszamy saldo
            print(f'Withdrawn {amount:.2f}. Balance: {balance:.2f}')   # potwierdzenie
    elif choice == '3':                                      # saldo
        print(f'Balance: {balance:.2f}')                     # wypisujemy saldo
    elif choice == '4':                                      # NOWE: sprawdzenie PIN
        entered_pin = input('Enter PIN: ')                   # wczytujemy PIN
        if entered_pin == pin:                               # porównujemy z zapisanym PIN-em
            print('PIN is correct')                          # PIN poprawny
        else:                                                # PIN błędny
            print('Incorrect PIN')                           # komunikat
    elif choice == '5':                                      # NOWE: zmiana PIN
        old_pin = input('Enter current PIN: ')               # najpierw prosimy o obecny PIN
        if old_pin == pin:                                   # obecny PIN poprawny
            new_pin = input('Enter new PIN (4 digits): ')    # wczytujemy nowy PIN
            if len(new_pin) == 4 and new_pin.isdigit():      # dokładnie 4 znaki i wszystkie to cyfry (isdigit)
                pin = new_pin                                # zapisujemy nowy PIN
                print('PIN changed')                         # potwierdzenie
            else:                                            # nowy PIN nie spełnia wymagań
                print('PIN must consist of exactly 4 digits')   # komunikat
        else:                                                # obecny PIN błędny
            print('Incorrect PIN')                           # nie pozwalamy zmienić PIN-u
    elif choice == '0':                                      # wyjście
        print('Goodbye!')                                    # pożegnanie
    else:                                                    # nieznana opcja
        print('Unknown option')                              # komunikat
