###
# Prints information about cities from a JSON file
#
import json                                                # moduł do plików JSON

# Open the JSON file in read mode
with open('cities.json', 'r', encoding='utf-8') as file:   # utf-8 jest potrzebne, bo nazwy miast mają polskie litery
    # Load the data from the JSON file into a variable
    data = json.load(file)                                 # plik zawiera listę słowników, więc data to lista

# Print the JSON data
for city in data:                                          # bierzemy po kolei każde miasto (słownik)
    for key, value in city.items():                        # bierzemy po kolei każdą parę w tym słowniku
        print(key, ':', value)                             # wypisujemy ją
    print()                                                # pusta linia między miastami
