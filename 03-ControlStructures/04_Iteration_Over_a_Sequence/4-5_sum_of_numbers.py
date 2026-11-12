###
# Calculates the sum of integer numbers in the range <5,10>
# (zmiany: zakres 5..10 oraz operator +=)
#
sum = 0                                                      # suma początkowa (uwaga: nazwa sum przesłania wbudowaną funkcję sum, ale tak jest w zadaniu)

for i in range(5,11):                                        # range(5,11) daje 5,6,...,10 (koniec jest wyłączony)
    sum += i                                                 # += to skrót od sum = sum + i

print(f'Sum is {sum}')                                      # wynik: 45
