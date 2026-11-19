###
# Calculates the number of lines, characters and words in a text file
#
file_name = input('File name: ')                           # wczytujemy nazwę pliku, np. pets.txt

try:                                                       # próbujemy otworzyć plik, który może nie istnieć
    with open(file_name, 'r', encoding='utf-8') as file:   # utf-8, bo teksty z internetu mają często znaki specjalne
        content = file.read()                              # wczytujemy cały plik
    print('Number of lines:', len(content.splitlines()))   # liczba linii = długość listy linii
    print('Number of characters:', len(content))           # liczba znaków = długość całego napisu (Entery też się liczą)
    print('Number of words:', len(content.split()))        # liczba słów = długość listy słów
except FileNotFoundError:                                  # jeśli pliku nie ma
    print('File', file_name, 'does not exist.')            # wypisujemy komunikat zamiast awarii
