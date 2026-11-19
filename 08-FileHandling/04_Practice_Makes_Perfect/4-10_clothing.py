###
# Prints products whose price is less than 60 and stock is less than 40
#
import csv                                            # moduł do plików CSV

with open('clothing.csv', 'r', newline='') as file:   # otwieramy plik z ubraniami
    reader = csv.reader(file)                         # każdą linię dostaniemy jako listę kolumn
    header = next(reader)                             # next() bierze pierwszy wiersz (nagłówki), żeby nie liczyć go jako produktu
    for row in reader:                                # pętla: bierzemy po kolei każdy produkt
        price = float(row[2])                         # kolumna 2 to cena; zamieniamy napis na liczbę
        stock = int(row[3])                           # kolumna 3 to liczba sztuk
        if price < 60 and stock < 40:                 # jeśli cena poniżej 60 i sztuk poniżej 40
            print(row[0], row[1], price, stock)       # wypisujemy nazwę, rozmiar, cenę i liczbę sztuk
