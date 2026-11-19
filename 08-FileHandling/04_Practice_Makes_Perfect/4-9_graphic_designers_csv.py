###
# Prints the first name, last name and email of people
# employed as 'Graphic Designer' (csv module)
#
import csv                                                # moduł csv ułatwia czytanie plików, w których dane są oddzielone przecinkami

print('GRAPHIC DESIGNERS')                                # nagłówek
print('=================')                                # linia pod nagłówkiem

with open('it_company.csv', 'r', newline='') as file:     # newline='' to zalecane ustawienie przy plikach CSV
    reader = csv.reader(file)                             # reader podaje każdą linię jako listę kolumn
    for row in reader:                                    # pętla: bierzemy po kolei każdy wiersz, np. ['Chris', 'Martin', 'chris.martin@example.com', 'Graphic Designer']
        if row[3] == 'Graphic Designer':                  # kolumna 3 (czwarta) to stanowisko
            print(row[0] + ' ' + row[1] + ',' + row[2])   # imię, spacja, nazwisko, przecinek, e-mail
