###
# Checking whether the number
# entered from the keyboard is even or odd
#
number = int(input('Enter number: '))                        # wczytujemy liczbę całkowitą

if number % 2 == 0:                                          # reszta z dzielenia przez 2 równa 0 oznacza liczbę parzystą
    print(f'{number} is even')                               # wypisujemy, że liczba jest parzysta
else:                                                        # w przeciwnym razie reszta wynosi 1
    print(f'{number} is odd')                                # wypisujemy, że liczba jest nieparzysta
