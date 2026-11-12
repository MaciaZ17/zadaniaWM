###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random                                      # importujemy moduł random
dice_roll_1 = random.randint(1,6)                  # rzut pierwszą kostką
dice_roll_2 = random.randint(1,6)                  # rzut drugą kostką
dice_roll_3 = random.randint(1,6)                  # rzut trzecią kostką
total = dice_roll_1 + dice_roll_2 + dice_roll_3    # suma oczek
print(f'Dice: {dice_roll_1}, {dice_roll_2}, {dice_roll_3}')   # wypisujemy wyniki rzutów
print(f'Sum: {total}')                             # wypisujemy sumę
