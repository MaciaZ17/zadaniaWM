###
# Draws the function y = sin(x) for angles from 0 to 360 degrees
#
import math                                   # dołączamy moduł math do sinusa
import matplotlib.pyplot as plt               # dołączamy moduł do wykresów

x = []                                        # pusta lista na kąty
y = []                                        # pusta lista na wartości sinusa

for angle in range(0, 361):                   # kąty od 0 do 360 stopni
    x = x + [angle]                           # doklejamy kąt do listy x
    y = y + [math.sin(math.radians(angle))]   # sin() liczy w radianach, więc najpierw zamieniamy stopnie

plt.plot(x, y)                                # rysujemy wykres
plt.title('y = sin(x)')                       # tytuł wykresu
plt.xlabel('degrees')                         # podpis osi poziomej
plt.show()                                    # pokazujemy okno z wykresem
