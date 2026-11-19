###
# Draws a line from position (1, 3) to position (8, 10)
# Najpierw zainstaluj moduł w terminalu: pip install matplotlib
#
import matplotlib.pyplot as plt   # dołączamy moduł do wykresów; "as plt" to krótsza nazwa

xpoints = [1, 8]                  # współrzędne x obu punktów
ypoints = [3, 10]                 # współrzędne y obu punktów
plt.plot(xpoints, ypoints)        # rysujemy linię przez punkty (1, 3) i (8, 10)
plt.show()                        # pokazujemy okno z wykresem
