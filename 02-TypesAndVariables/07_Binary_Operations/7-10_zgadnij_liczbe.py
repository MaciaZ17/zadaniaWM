###
# Gra: komputer rzuca kostką, a użytkownik zgaduje liczbę.
#
import random                                      # importujemy moduł random
# COMPUTER TURN
computer = random.randint(1,6)                     # komputer losuje liczbę od 1 do 6
# YOUR TURN
you = int(input('Guess the number (1-6): '))       # int() jest konieczne - input zwraca tekst, a porównanie "3" == 3 zawsze daje False
won = you == computer                              # porównujemy zgadnięcie z wylosowaną liczbą
print(f'Computer rolled: {computer}')              # pokazujemy, co wypadło (pomaga w testowaniu)
print(f'You won: {won}')                           # wypisujemy True/False
