###
# Prints a numbered list of countries from a text file
#
number = 1                                   # numer na liście, zaczynamy od 1
with open('countries.txt', 'r') as file:     # otwieramy plik do odczytu
    for line in file:                        # pętla: bierzemy po kolei każdą linię
        print(f'{number}. {line}', end='')   # wypisujemy numer, kropkę i linię, np. 1. Poland, Warsaw, 38265000
        number = number + 1                  # następna linia dostanie numer o 1 większy
