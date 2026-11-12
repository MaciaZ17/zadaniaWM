###
# Tabliczka mnożenia od 1 do 10 dla podanej liczby
#
number = int(input('Enter number: '))                        # wczytujemy liczbę
for i in range(1, 11):                                       # mnożnik od 1 do 10
    print(f'{number} x {i} = {number * i}')                  # wypisujemy działanie i wynik
