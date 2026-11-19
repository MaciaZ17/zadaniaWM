###
# Writes data about a favourite movie to the favourite.json file
#
import json                                                   # moduł do plików JSON

favourite = {
    "title": "Interstellar",
    "director": "Christopher Nolan",
    "year": 2014,
    "genre": "Science fiction",
    "duration_minutes": 169,
    "main_actors": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"]
}                                                             # słownik opisujący ulubiony film

with open('favourite.json', 'w', encoding='utf-8') as file:   # otwieramy plik do zapisu
    json.dump(favourite, file, indent=4)                      # zapisujemy słownik jako JSON

print('Saved to favourite.json')                              # informujemy, że zapis się udał
