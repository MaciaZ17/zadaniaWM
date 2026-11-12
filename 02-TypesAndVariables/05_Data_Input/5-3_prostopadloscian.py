###
# A program that calculates the volume
# and surface area of a cuboid with sides a, b, and c.
# UWAGA: w treści zadania wyniki dla a=3,b=4,c=5 są zamienione miejscami.
# Poprawnie: objętość = 60, pole powierzchni = 94.
# Dla a=8,b=1,c=2: objętość = 16, pole powierzchni = 52.
#
a = int(input('a='))                               # wczytujemy bok a i od razu zamieniamy na int
b = int(input('b='))                               # wczytujemy bok b
c = int(input('c='))                               # wczytujemy bok c
volume = a * b * c                                 # objętość = a * b * c
surface = 2 * (a*b + a*c + b*c)                    # pole = suma pól 6 ścian: 2*(ab + ac + bc)
print(f'Volume: {volume}')                         # wypisujemy objętość
print(f'Surface area: {surface}')                  # wypisujemy pole powierzchni
