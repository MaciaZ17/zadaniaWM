###
# Calculates the number of even values in the array (while loop)
#
arr = [34, 7, 19, 4, 21, 8]              # lista liczb

count = 0                                # licznik liczb parzystych, na początku 0
i = 0                                    # i to indeks elementu, zaczynamy od 0
while i < len(arr):                      # powtarzamy, dopóki nie przejdziemy całej listy
    if arr[i] % 2 == 0:                  # jeśli reszta z dzielenia przez 2 to 0, liczba jest parzysta
        count = count + 1                # zwiększamy licznik
    i = i + 1                            # przechodzimy do następnego elementu

print('Number of even values:', count)   # wypisujemy wynik (3)
