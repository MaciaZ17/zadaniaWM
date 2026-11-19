###
# Calculates, prints and saves to a text file integers from 1 to 100
# and their second and third powers
#
file_name = 'powers.txt'                  # plik, który powstanie

with open(file_name, 'w') as file:        # otwieramy plik do zapisu
    for n in range(1, 101):               # liczby od 1 do 100
        line = f'{n},{n ** 2},{n ** 3}'   # liczba, jej kwadrat i sześcian oddzielone przecinkami, np. 3,9,27
        print(line)                       # wypisujemy na ekranie
        file.write(line + '\n')           # i zapisujemy do pliku z przejściem do nowej linii
