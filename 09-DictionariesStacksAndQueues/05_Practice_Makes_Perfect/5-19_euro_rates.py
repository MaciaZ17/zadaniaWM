###
# Displays Euro exchange rates from the euro.json file (NBP data)
#
# Plik euro.json pobrano z: https://api.nbp.pl/api/exchangerates/rates/c/eur/last/10/?format=json
# W pliku: "rates" to lista kursów; bid = kurs kupna, ask = kurs sprzedaży.
import json                                                           # moduł do plików JSON

with open('euro.json', 'r', encoding='utf-8') as file:                # otwieramy plik z kursami
    data = json.load(file)                                            # wczytujemy go jako słownik

print(f'{"Date":<16}{"Buying Rate":<16}Selling Rate')                 # nagłówek; :<16 wyrównuje do lewej na 16 miejscach
print('============================================')                 # linia pod nagłówkiem
for rate in data['rates']:                                            # bierzemy po kolei każdy dzień z listy kursów
    print(f'{rate["effectiveDate"]:<16}{rate["bid"]:<16.4f}{rate["ask"]:.4f}')  # .4f to 4 miejsca po kropce
