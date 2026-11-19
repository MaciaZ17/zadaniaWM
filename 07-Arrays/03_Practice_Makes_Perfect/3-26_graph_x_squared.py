###
# Draws the graph of the function f(x) = x^2 - 3
#
import matplotlib.pyplot as plt   # dołączamy moduł do wykresów

x = []                            # pusta lista na wartości x
y = []                            # pusta lista na wartości y

# create x values
for n in range(-100, 101):        # liczby od -100 do 100
    x = x + [n]                   # doklejamy liczbę na koniec listy x

# create y values
for n in x:                       # bierzemy po kolei każdą wartość x
    y = y + [n ** 2 - 3]          # liczymy f(x) = x do kwadratu minus 3 i doklejamy do listy y

# print chart
plt.plot(x, y)                    # rysujemy wykres: x poziomo, y pionowo
plt.title('f(x) = x^2 - 3')       # tytuł wykresu
plt.show()                        # pokazujemy okno z wykresem
