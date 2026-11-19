###
# Tries to print the contents of a file inside a try-except block
# (the program continues even when an error occurs)
#
file_name = 'missing_file.txt'                    # takiego pliku nie ma na dysku

try:                                              # try: próbujemy wykonać kod, który może dać błąd
    with open(file_name, 'r') as file:            # próba otwarcia pliku
        print(file.read())                        # jeśli się uda, wypisujemy treść
except FileNotFoundError:                         # except: ten kod wykona się, gdy pliku nie ma
    print('File', file_name, 'does not exist.')   # zamiast awarii wypisujemy komunikat

print('End of program')                           # program działa dalej i dochodzi do końca
