###
# Writes Seven Wonders of the World to a file
#
seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]                                        # lista siedmiu cudów świata

# Name of the file to write to
file_name = 'seven_wonders.txt'          # nazwa pliku, który powstanie

# Sort data alphabetically
sorted_wonders = sorted(seven_wonders)   # sorted() układa nazwy alfabetycznie

# Write data to the file
with open(file_name, 'w') as file:       # otwieramy plik do zapisu
    for item in sorted_wonders:          # pętla: bierzemy po kolei każdą nazwę
        file.write(item + '\n')          # zapisujemy nazwę i przechodzimy do nowej linii

print('Saved to', file_name)             # informujemy, że zapis się udał
