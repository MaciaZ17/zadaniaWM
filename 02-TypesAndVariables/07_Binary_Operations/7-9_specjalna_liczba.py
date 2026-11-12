###
# Czy wylosowana liczba oczek to 1 lub 6?
#
import random                                      # importujemy moduł random
dice = random.randint(1,6)                         # rzut kostką
special = dice == 1 or dice == 6                   # or = wystarczy, że jeden warunek jest prawdziwy
print(f'Dice rolled: {dice}')                      # wypisujemy wynik rzutu
print(f'Special number (1 or 6): {special}')       # wypisujemy True/False
