###
# Calculates the number of days in a month
# (zakładamy, że luty zawsze ma 28 dni)
#
month = int(input('Enter month number (1..12): '))           # wczytujemy numer miesiąca
days = 0                                                     # liczba dni (na razie 0)

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:   # miesiące 31-dniowe
    days = 31                                                # 31 dni
elif month==4 or month==6 or month==9 or month==11:          # miesiące 30-dniowe
    days = 30                                                # 30 dni
elif month==2:                                               # luty
    days = 28                                                # 28 dni (założenie z treści)

if days == 0:                                                # jeśli nadal 0, to numer miesiąca był błędny
    print('Incorrect month number')                          # komunikat o błędzie
else:                                                        # numer miesiąca poprawny
    print(f'Month {month} has {days} days')                  # wypisujemy wynik
