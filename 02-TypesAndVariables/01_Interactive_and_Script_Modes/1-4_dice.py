###
# The program simulates five dice rolls.
# (Program symuluje pięć rzutów kostką.)
#
import random                                # importujemy moduł random, który zawiera generator liczb losowych
print("Dice rolling simulator")              # wypisujemy nagłówek programu
for i in range(5):                           # pętla wykona się 5 razy (i = 0,1,2,3,4)
    dice_roll = random.randint(1,6)          # losujemy liczbę całkowitą od 1 do 6 (włącznie z oboma końcami)
    print(dice_roll, end=" ")                # wypisujemy wynik; end=" " daje spację zamiast przejścia do nowej linii
