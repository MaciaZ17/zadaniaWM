###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
# Testy: 12 -> 4, 10 -> 4, 9 -> 3, 1 -> 1
#
month = int(input('Enter month number (1..12): '))           # wczytujemy numer miesiąca

if month >= 10:                                              # miesiące 10, 11, 12
    quarter = 4                                              # czwarty kwartał
elif month >= 7:                                             # tu trafiają miesiące 7, 8, 9 (10+ zostało już obsłużone wyżej)
    quarter = 3                                              # trzeci kwartał
elif month >= 4:                                             # miesiące 4, 5, 6
    quarter = 2                                              # drugi kwartał
else:                                                        # miesiące 1, 2, 3
    quarter = 1                                              # pierwszy kwartał

print(f'Month {month} is in quarter {quarter}')              # wypisujemy wynik
