###
# Wypisuje N pierwszych liczb pierwszych.
#
N = int(input('Enter N: '))                                  # ile liczb pierwszych wypisać
found = 0                                                    # ile znaleziono do tej pory
candidate = 2                                                # sprawdzana liczba (zaczynamy od 2, bo to najmniejsza pierwsza)
print('Prime numbers:', end=' ')                             # nagłówek bez przejścia do nowej linii

while found < N:                                             # szukamy, aż znajdziemy N liczb
    is_prime = True                                          # zakładamy, że candidate jest pierwsza
    for divisor in range(2, candidate):                      # sprawdzamy dzielniki od 2 do candidate-1
        if candidate % divisor == 0:                         # jeśli dzieli się bez reszty
            is_prime = False                                 # to nie jest pierwsza
            break                                            # dalsze sprawdzanie nie ma sensu
    if is_prime:                                             # jeśli nikt jej nie podzielił
        print(candidate, end=' ')                            # wypisujemy
        found += 1                                           # zwiększamy licznik znalezionych
    candidate += 1                                           # przechodzimy do następnej liczby
print()                                                      # nowa linia na końcu
