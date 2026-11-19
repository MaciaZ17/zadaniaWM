###
# Separates even and odd numbers: even numbers first, then odd numbers
#
arr = [7, 9, 2, 4, 5, 6]              # lista liczb
print('arr =', arr)                   # wypisujemy listę przed zmianą

even_numbers = []                     # pusta lista na liczby parzyste
odd_numbers = []                      # pusta lista na liczby nieparzyste
for number in arr:                    # bierzemy po kolei każdą liczbę
    if number % 2 == 0:               # jeśli jest parzysta
        even_numbers.append(number)   # dopisujemy ją do parzystych
    else:                             # w przeciwnym razie
        odd_numbers.append(number)    # dopisujemy ją do nieparzystych

arr = even_numbers + odd_numbers      # + skleja dwie listy w jedną: najpierw parzyste, potem nieparzyste
print('arr =', arr)                   # wypisujemy wynik: [2, 4, 6, 7, 9, 5]
