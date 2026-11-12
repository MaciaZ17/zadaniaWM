###
# Pole trójkąta (a=5, h=4) oraz średnia arytmetyczna liczb 7, 12 i 31.
# Wersja skryptowa zadań z trybu interaktywnego.
#
a = 5                                   # podstawa trójkąta
h = 4                                   # wysokość trójkąta
pole = a * h / 2                        # wzór na pole trójkąta: (podstawa * wysokość) / 2
print("Pole trójkąta:", pole)           # wypisujemy wynik (10.0)
srednia = (7 + 12 + 31) / 3             # nawiasy są konieczne, żeby najpierw dodać liczby, a potem podzielić przez ich ilość
srednia = round(srednia, 2)             # zaokrąglamy wynik do 2 miejsc po przecinku
print("Średnia arytmetyczna:", srednia) # wypisujemy wynik (16.67)
