###
# Calculates how many registered cars come from each province of Poland
#
import csv                                                            # moduł do plików CSV

# Słownik provinces: pierwsza litera rejestracji -> nazwa województwa
# Słownik counts: pierwsza litera rejestracji -> liczba aut
provinces = {}                                                        # pusty słownik na województwa
counts = {}                                                           # pusty słownik na liczby aut

with open('province.csv', 'r', encoding='utf-8', newline='') as file:  # utf-8, bo nazwy mają polskie litery
    reader = csv.reader(file)                                         # każdą linię dostaniemy jako listę kolumn
    next(reader)                                                      # pomijamy pierwszą linię z nagłówkami
    for row in reader:                                                # bierzemy po kolei każde województwo, np. ['K', 'małopolskie']
        provinces[row[0]] = row[1]                                    # litera to klucz, nazwa województwa to wartość
        counts[row[0]] = 0                                            # na początku każde województwo ma 0 aut

with open('vehicle.txt', 'r') as file:                                # otwieramy plik z rejestracjami
    for line in file:                                                 # bierzemy po kolei każdą rejestrację
        letter = line.strip()[0]                                      # strip() usuwa Enter, [0] bierze pierwszą literę
        if letter in counts:                                          # jeśli taka litera jest w słowniku
            counts[letter] = counts[letter] + 1                       # zwiększamy licznik tego województwa

for letter, name in provinces.items():                                # bierzemy po kolei każde województwo
    print(name, ':', counts[letter])                                  # wypisujemy nazwę i liczbę aut
