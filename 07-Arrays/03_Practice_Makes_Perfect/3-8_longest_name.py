###
# Prints the longest name
#
names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']   # lista imion

longest = names[0]                                                  # na początku zakładamy, że pierwsze imię jest najdłuższe
for name in names:                                                  # bierzemy po kolei każde imię
    if len(name) > len(longest):                                    # jeśli ma więcej liter niż dotychczas najdłuższe
        longest = name                                              # zapamiętujemy je

print('Names:', end=' ')                                            # tekst bez przechodzenia do nowej linii
for name in names:                                                  # bierzemy po kolei każde imię
    print(name, end=' ')                                            # wypisujemy je ze spacją
print()                                                             # nowa linia
print('Longest name:', longest)                                     # wypisujemy najdłuższe imię (Celestyna)
