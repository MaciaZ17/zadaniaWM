###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0                                                      # suma początkowa

for i in range(1,11):                                        # liczby od 1 do 10
    if not i % 2 == 0:                                       # jeśli liczba NIE jest parzysta
        continue                                             # continue pomija resztę obiegu i przechodzi do następnej liczby
    sum += i                                                 # dodajemy tylko liczby parzyste

print(f'Sum of even numbers in the range <1,10> is {sum}')   # wynik: 30 (2+4+6+8+10)
