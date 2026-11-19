###
# Computes the second power of each array element
#
arr = [8, 2, 5, 1, 9]            # lista liczb

print('Array:', end=' ')         # tekst bez przechodzenia do nowej linii
for value in arr:                # bierzemy po kolei każdy element
    print(value, end=' ')        # wypisujemy go ze spacją
print()                          # nowa linia

print('2nd power:', end=' ')     # tekst bez przechodzenia do nowej linii
for value in arr:                # bierzemy po kolei każdy element
    print(value ** 2, end=' ')   # ** 2 to potęga druga, np. 8 ** 2 = 64
print()                          # nowa linia
