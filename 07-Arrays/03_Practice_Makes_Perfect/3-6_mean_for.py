###
# Prints the array and the arithmetic mean of its values (for loop)
#
arr = [15, 8, 31, 47, 2, 19]                # lista liczb

total = 0                                   # suma, na początku 0
for value in arr:                           # bierzemy po kolei każdy element
    total = total + value                   # dodajemy go do sumy
mean = total / len(arr)                     # średnia = suma / liczba elementów

print('Array:', arr)                        # wypisujemy listę
print('Arithmetic mean:', round(mean, 2))   # wypisujemy średnią zaokrągloną do 2 miejsc (20.33)
