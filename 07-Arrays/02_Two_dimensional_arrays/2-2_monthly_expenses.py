###
# Calculates expenses for each category, each week and the whole month
#
# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]

# Calculates expenses
category_totals = [0, 0, 0]                                 # sumy kategorii: [jedzenie, transport, opłaty], na początku zera
week_totals = []                                            # pusta lista, dopiszemy do niej sumę każdego tygodnia
month_total = 0                                             # suma całego miesiąca

for week in monthly_expenses:                               # pętla: bierzemy po kolei każdy tydzień (wiersz)
    week_sum = 0                                            # suma tego tygodnia, na początku 0
    for i in range(len(week)):                              # i to numer kategorii: 0, 1, 2
        week_sum = week_sum + week[i]                       # dodajemy wydatek do sumy tygodnia
        category_totals[i] = category_totals[i] + week[i]   # i do sumy jego kategorii
    week_totals.append(week_sum)                            # append() dopisuje sumę tygodnia na koniec listy
    month_total = month_total + week_sum                    # dodajemy sumę tygodnia do sumy miesiąca

# Print expenses
print('MONTHLY EXPENSES')                                   # nagłówek
print('----------------')                                   # linia pod nagłówkiem
print('Food:', category_totals[0])                          # suma jedzenia (810)
print('Transport:', category_totals[1])                     # suma transportu (230)
print('Utilities:', category_totals[2])                     # suma opłat (410)
print('Week 1:', week_totals[0])                            # suma tygodnia 1 (350)
print('Week 2:', week_totals[1])                            # tygodnia 2 (350)
print('Week 3:', week_totals[2])                            # tygodnia 3 (380)
print('Week 4:', week_totals[3])                            # tygodnia 4 (370)
print('---------------')                                    # linia oddzielająca
print('TOTAL:', month_total)                                # suma miesiąca (1450)
