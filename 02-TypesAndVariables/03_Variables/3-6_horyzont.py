###
# Odległość do horyzontu: d = 3.57 * sqrt(h)
# d - odległość w km, h - wysokość obserwatora w metrach
#
import math                                        # potrzebujemy math.sqrt do pierwiastka
h = float(input('Enter height in meters: '))       # wczytujemy wysokość i zamieniamy tekst na float (może być np. 1.75)
d = 3.57 * math.sqrt(h)                            # wzór z treści zadania
print(f'Distance to the horizon: {d:.2f} km')      # wypisujemy wynik z dokładnością do 2 miejsc
# Wyniki do zadania:
# a) plaża, wzrost np. 1.75 m  -> ok. 4.72 km (horyzont jest naprawdę blisko!)
# b) okno hotelu na wysokości 20 m -> ok. 15.97 km
