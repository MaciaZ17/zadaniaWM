###
# Prints the contents of the array in reverse order
#
arr = [15, 8, 31, 47, 2, 19]       # lista liczb

print('existed array:', end=' ')   # tekst bez przechodzenia do nowej linii
for value in arr:                  # bierzemy po kolei każdy element
    print(value, end=' ')          # wypisujemy go ze spacją
print()                            # nowa linia

print('reverse array:', end=' ')   # tekst bez przechodzenia do nowej linii
i = len(arr) - 1                   # zaczynamy od indeksu ostatniego elementu
while i >= 0:                      # idziemy do tyłu, aż do indeksu 0
    print(arr[i], end=' ')         # wypisujemy element ze spacją
    i = i - 1                      # cofamy się o jeden element
print()                            # nowa linia
