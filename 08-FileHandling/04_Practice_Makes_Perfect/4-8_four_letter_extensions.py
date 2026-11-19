###
# Prints file names whose extensions have exactly four characters
#
import re                                  # moduł do wyrażeń regularnych

with open('files.txt', 'r') as file:       # otwieramy plik z nazwami plików
    for line in file:                      # pętla: bierzemy po kolei każdą linię
        name = line.strip()                # strip() usuwa znak nowej linii i spacje z końców
        if re.search(r'\.\w{4}$', name):   # kropka, dokładnie 4 litery lub cyfry, koniec napisu ($)
            print(name)                    # wypisujemy pasującą nazwę
