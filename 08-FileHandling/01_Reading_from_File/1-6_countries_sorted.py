###
# Reads the entire contents of a file
# and prints the countries sorted alphabetically
#
def read_from_file(name):                        # funkcja czyta cały plik; name to nazwa pliku
    with open(name, 'r') as file:                # otwieramy plik do odczytu
        content = file.read()                    # read() wczytuje cały plik jako jeden napis
    return content                               # funkcja oddaje zawartość pliku

# reads the entire file
file_content = read_from_file('countries.txt')   # wczytujemy plik countries.txt

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines()           # splitlines() dzieli napis na listę linii

# sorts the array alphabetically
sorted_lines = sorted(file_lines)                # sorted() układa linie alfabetycznie

# prints the array
for line in sorted_lines:                        # pętla: bierzemy po kolei każdą linię
    print(line)                                  # wypisujemy ją (splitlines usunął znaki nowej linii, więc zwykły print)
