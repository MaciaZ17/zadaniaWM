###
# Prints the text from a file and counts the number of words
#
word_count = 0                                 # licznik słów, na początku 0
with open('pets.txt', 'r') as file:            # otwieramy plik do odczytu
    for line in file:                          # pętla: bierzemy po kolei każdą linię
        print(line, end='')                    # wypisujemy linię (ma już na końcu znak nowej linii)
        words = line.split()                   # split() dzieli linię na listę słów w miejscach spacji
        word_count = word_count + len(words)   # len() podaje liczbę słów w linii, dodajemy ją do sumy

print()                                        # pusta linia dla czytelności
print('Number of words:', word_count)          # wypisujemy liczbę wszystkich słów
