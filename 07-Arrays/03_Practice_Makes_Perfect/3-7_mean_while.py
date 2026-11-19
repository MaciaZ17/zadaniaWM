###
# Prints the array and the arithmetic mean of its values (while loop)
#
arr = [15, 8, 31, 47, 2, 19]                # lista liczb

total = 0                                   # suma, na początku 0
i = 0                                       # i to indeks elementu, zaczynamy od 0
while i < len(arr):                         # powtarzamy, dopóki nie przejdziemy całej listy
    total = total + arr[i]                  # dodajemy element do sumy
    i = i + 1                               # przechodzimy do następnego elementu
mean = total / len(arr)                     # średnia = suma / liczba elementów

print('Array:', arr)                        # wypisujemy listę
print('Arithmetic mean:', round(mean, 2))   # wypisujemy średnią zaokrągloną do 2 miejsc (20.33)
