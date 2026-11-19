###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
def weekday(n):                                               # funkcja zwraca nazwę dnia; n to numer dnia od 1 do 7
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]   # lista nazw dni (indeksy od 0 do 6)
    return weekdays[n - 1]                                    # odejmujemy 1, bo dzień 1 ma w liście indeks 0

print('Day 1 is', weekday(1))                                 # wypisujemy nazwę dnia 1 (Monday)
print('Day 4 is', weekday(4))                                 # dnia 4 (Thursday)
print('Day 7 is', weekday(7))                                 # dnia 7 (Sunday)
