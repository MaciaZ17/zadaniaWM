###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = 70                                     # prędkość w km/h
speed_ms = speed_kmh * 1000 / 3600                 # 1 km = 1000 m, 1 h = 3600 s, więc mnożymy przez 1000 i dzielimy przez 3600
speed_ms = round(speed_ms, 2)                      # zaokrąglamy do 2 miejsc po przecinku (19.44)
print(speed_kmh, "km/h = ", speed_ms, "m/s")       # wypisujemy wynik
