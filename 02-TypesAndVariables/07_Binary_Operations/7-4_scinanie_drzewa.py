###
# Drzewo można ściąć, gdy jego średnica wynosi co najmniej 50 cm.
# Mamy obwód: obwód = pi * średnica, więc średnica = obwód / pi.
# Wyniki: drzewo 1 (160) TAK, drzewo 2 (90) NIE, drzewo 3 (230) TAK, drzewo 4 (120) NIE
#
import math                                        # potrzebujemy math.pi (liczba pi)
circumference = float(input('Enter tree circumference in cm: '))   # wczytujemy obwód w cm
diameter = circumference / math.pi                 # obliczamy średnicę z obwodu
can_be_cut = diameter >= 50                        # co najmniej 50 cm -> True, inaczej False
print(f'Tree can be cut down: {can_be_cut}')       # wypisujemy wynik
