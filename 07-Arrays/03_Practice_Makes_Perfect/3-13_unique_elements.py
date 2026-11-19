###
# Prints all unique elements in an array (elements that appear only once)
#
arr = [2, 3, 2, 5, 8, 1, 9, 8]       # lista liczb

print('Array:', end=' ')             # tekst bez przechodzenia do nowej linii
for value in arr:                    # bierzemy po kolei każdy element
    print(value, end=' ')            # wypisujemy go ze spacją
print()                              # nowa linia

print('Unique elements:', end=' ')   # tekst bez przechodzenia do nowej linii
for value in arr:                    # bierzemy po kolei każdy element
    if arr.count(value) == 1:        # count() mówi, ile razy element jest w liście; 1 znaczy, że jest unikalny
        print(value, end=' ')        # wypisujemy go
print()                              # nowa linia (wynik: 3 5 1 9)
