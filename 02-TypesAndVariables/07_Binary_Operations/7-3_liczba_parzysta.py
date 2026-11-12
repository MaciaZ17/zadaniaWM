###
# Czy liczba jest parzysta? Testy: 24 True, 8 True, 31 False, 5 False
#
number = int(input('Enter number: '))              # wczytujemy liczbę całkowitą
even = number % 2 == 0                             # % daje resztę z dzielenia; parzysta = reszta 0. Podwójne == to porównanie
print(f'Number is even: {even}')                   # wypisujemy True lub False
