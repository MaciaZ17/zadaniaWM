###
# Calculates the total number of hours in the winter semester
#
winter_semester = {
    "math": 60,
    "programming": 30,
    "history": 15
}                                                                     # przedmiot to klucz, liczba godzin to wartość

total = 0                                                             # suma godzin, na początku 0
for hours in winter_semester.values():                                # values() daje same wartości (liczby godzin)
    total = total + hours                                             # dodajemy je do sumy

print('The total number of hours in the winter semester is', total)   # wypisujemy wynik (105)
