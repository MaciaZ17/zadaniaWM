###
# Prints information about a computer from a JSON file
#
import json                                                  # moduł do plików JSON

# Open the JSON file in read mode
with open('computer.json', 'r', encoding='utf-8') as file:   # otwieramy plik do odczytu
    # Load the data from the JSON file into a variable
    data = json.load(file)                                   # json.load() zamienia plik na słownik

# Print the JSON data
for key, value in data.items():                              # bierzemy po kolei każdą parę klucz : wartość
    print(key, ':', value)                                   # wypisujemy ją
