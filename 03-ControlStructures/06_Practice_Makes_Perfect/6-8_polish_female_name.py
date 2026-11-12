###
# Polskie imiona żeńskie zwykle kończą się na "a".
#
name = input('Enter name: ')                                 # wczytujemy imię
last_letter = name[len(name) - 1]                            # ostatni znak ma indeks długość-1 (indeksy zaczynają się od 0)
if last_letter == 'a':                                       # sprawdzamy, czy ostatnia litera to a
    print(f'{name} -- Polish female name')                   # wypisujemy komunikat tylko dla imion żeńskich
