###
# Prędkość na autostradzie musi być między 40 a 140 km/h (włącznie).
#
speed = int(input('Enter vehicle speed: '))        # wczytujemy prędkość jako liczbę całkowitą
speed_ok = speed >= 40 and speed <= 140            # and = oba warunki muszą być prawdziwe jednocześnie
print(f'Speed is valid: {speed_ok}')               # wypisujemy wynik (np. 158 -> False)
