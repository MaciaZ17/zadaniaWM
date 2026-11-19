###
# Records voting results in the voting.json file
#
import json                                                      # moduł do plików JSON

# Read the contents of the json file
try:                                                             # próbujemy wczytać plik
    with open('voting.json', 'r', encoding='utf-8') as file:     # otwieramy plik z głosami
        votes = json.load(file)                                  # json.load() zamienia zawartość pliku na słownik
except FileNotFoundError:                                        # jeśli pliku jeszcze nie ma
    votes = {}                                                   # zaczynamy od pustego słownika

# Vote for a person
person_name = input('Name of the person you are voting for: ')   # wczytujemy imię
if person_name in votes:                                         # jeśli ta osoba już ma głosy
    votes[person_name] = votes[person_name] + 1                  # dodajemy jej 1 głos
else:                                                            # jeśli to nowa osoba
    votes[person_name] = 1                                       # dodajemy ją z 1 głosem

# Save voting data to json file
with open('voting.json', 'w', encoding='utf-8') as file:         # otwieramy plik do zapisu
    json.dump(votes, file, indent=4)                             # json.dump() zapisuje słownik do pliku; indent=4 robi czytelne wcięcia

print('Current results:')                                        # nagłówek
for name, count in votes.items():                                # bierzemy po kolei każdą osobę i jej głosy
    print(name, ':', count)                                      # wypisujemy wyniki
