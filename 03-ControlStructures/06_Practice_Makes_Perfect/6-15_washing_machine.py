###
# Calculates and prints the total washing time.
# kurtka 40 min, bielizna 70 min, buty 20 min, dodatkowe płukanie 15 min, dodatkowe wirowanie 9 min
# Przykład: buty + płukanie = 35 minut
#
total_washing_time = 0                                       # łączny czas prania
program_ok = True                                            # flaga poprawności programu
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')   # wybór programu
extra_rinse = input('Extra rinse? (y/n)')                    # czy dodatkowe płukanie
extra_spin = input('Extra spin? (y/n)')                      # czy dodatkowe wirowanie

if program == 'j':                                           # kurtka
    total_washing_time = 40                                  # 40 minut
elif program == 'u':                                         # bielizna
    total_washing_time = 70                                  # 70 minut
elif program == 's':                                         # buty
    total_washing_time = 20                                  # 20 minut
else:                                                        # nieznany program
    program_ok = False                                       # oznaczamy błąd

if program_ok:                                               # liczymy dalej tylko dla poprawnego programu
    if extra_rinse == 'y':                                   # dodatkowe płukanie
        total_washing_time += 15                             # +15 minut
    if extra_spin == 'y':                                    # dodatkowe wirowanie
        total_washing_time += 9                              # +9 minut
    print(f'Total washing time: {total_washing_time} minutes')   # wynik
else:                                                        # błędny program
    print('Unknown washing program')                         # komunikat
