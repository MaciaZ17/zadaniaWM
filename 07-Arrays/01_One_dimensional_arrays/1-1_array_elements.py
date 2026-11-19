###
# Prints some array elements
#
# Elementy listy mają numery (indeksy) liczone od 0: arr[0] to pierwszy, arr[1] drugi itd.
arr = [2, 3, 7, 5, 4]                                                 # tworzymy listę z pięcioma liczbami

print(arr)                                                            # wypisujemy całą listę
print('Number of elements', len(arr))                                 # len() podaje liczbę elementów (5)
print('First value', arr[0])                                          # pierwszy element ma indeks 0 (2)
print('Second value', arr[1])                                         # drugi element ma indeks 1 (3)
print('Last value', arr[len(arr) - 1])                                # ostatni ma indeks o 1 mniejszy niż liczba elementów (4)
print('Last but one value', arr[len(arr) - 2])                        # przedostatni: indeks o 2 mniejszy niż liczba elementów (5)
print('Sum of the first and last value', arr[0] + arr[len(arr) - 1])  # dodajemy pierwszy i ostatni (2 + 4 = 6)
print('Middle value', arr[len(arr) // 2])                             # środkowy: 5 // 2 = 2, więc arr[2] (7)

print('All values:', end=' ')                                         # end=' ' sprawia, że po tekście jest spacja zamiast przejścia do nowej linii
for value in arr:                                                     # pętla: bierzemy po kolei każdy element listy
    print(value, end=' ')                                             # wypisujemy element i spację
print()                                                               # na końcu przechodzimy do nowej linii
