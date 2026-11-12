###
# Checks if the given day number of the month is correct
# Testy: miesiąc 3 dzień 17 -> OK, miesiąc 9 dzień 31 -> błąd, miesiąc 2 dzień 30 -> błąd
#
month = int(input('Enter month number (1..12): '))           # wczytujemy numer miesiąca
day = int(input('Enter the day number of the month: '))      # wczytujemy numer dnia
day_ok = False                                               # zakładamy, że dzień jest błędny

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:   # miesiące 31-dniowe
    if day >=1 and day <= 31:                                # dzień musi być w zakresie 1..31
        day_ok = True                                        # dzień poprawny
elif month==4 or month==6 or month==9 or month==11:          # miesiące 30-dniowe
    if day >=1 and day <= 30:                                # dzień musi być w zakresie 1..30
        day_ok = True                                        # dzień poprawny
elif month==2:                                               # luty (28 dni)
    if day >=1 and day <= 28:                                # dzień musi być w zakresie 1..28
        day_ok = True                                        # dzień poprawny

message = f'Day {day} for the month {month}'                 # wspólny początek komunikatu
if day_ok:                                                   # dzień poprawny
    print(f'{message} is correct')                           # f przed apostrofem - bez niego nie podstawiłoby wartości
else:                                                        # w oryginale brakowało dwukropka po else
    print(f'{message} is incorrect')                         # dzień błędny
