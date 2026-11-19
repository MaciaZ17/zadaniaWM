###
# Calculates the total number of parked cars
#
def read_from_file(name):                       # funkcja czyta cały plik
    with open(name) as file:                    # bez 'r' plik też otwiera się do odczytu (to ustawienie domyślne)
        content = file.read()                   # wczytujemy cały plik
    return content                              # funkcja oddaje zawartość

# reads the entire file and splits lines into array
file_content = read_from_file('car_park.txt')   # wczytujemy plik z liczbą aut
file_lines = file_content.splitlines()          # dzielimy na linie; każda linia to jeden dzień

# calculates the total number of cars parked
total = 0                                       # suma aut, na początku 0
for line in file_lines:                         # pętla: bierzemy po kolei każdą linię
    total += int(line)                          # zamieniamy napis na liczbę i dodajemy do sumy (+= to skrót od total = total + ...)

print('Total cars parked:', total)              # wypisujemy wynik (645)
