###
# Prints information about dogs younger than 5 years
#
import json                                                           # moduł do plików JSON

with open('dogs.json', 'r', encoding='utf-8') as file:                # otwieramy plik z psami
    dogs = json.load(file)                                            # lista słowników, każdy opisuje jednego psa

for dog in dogs:                                                      # bierzemy po kolei każdego psa
    if dog['age'] < 5:                                                # jeśli ma mniej niż 5 lat
        print(dog['name'], '-', dog['breed'], '-', dog['age'], 'years')  # wypisujemy imię, rasę i wiek
