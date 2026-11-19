###
# Generates and prints a random number between 1 and 6,
# similar to rolling a dice
#
import random                 # dołączamy moduł random, który umie losować liczby

dice = random.randint(1, 6)   # losujemy liczbę od 1 do 6 (1 i 6 też mogą wypaść)
print('You rolled:', dice)    # wypisujemy wylosowaną liczbę
