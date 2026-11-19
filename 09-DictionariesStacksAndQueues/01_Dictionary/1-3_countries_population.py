###
# Creates an array of 5 dictionaries (country and population) and prints it
#
countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 68000000},
    {"name": "Spain", "population": 48000000},
    {"name": "Italy", "population": 59000000}
]                                                           # lista, w której każdy element to słownik z nazwą kraju i liczbą ludności

print(f'{"COUNTRY":<9}POPULATION')                          # nagłówek; :<9 wyrównuje tekst do lewej na 9 miejscach
for country in countries:                                   # bierzemy po kolei każdy słownik z listy
    print(f'{country["name"]:<9}{country["population"]}')   # wypisujemy nazwę (9 miejsc) i liczbę ludności
