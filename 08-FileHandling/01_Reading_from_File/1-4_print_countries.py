###
# Opens a text file, reads its contents line by line
# and prints each line
#
# with open(...) as file: otwiera plik i sam go zamyka, gdy skończy się wcięty blok.
with open('countries.txt', 'r') as file:   # otwieramy plik countries.txt do odczytu ('r' = read)
    for line in file:                      # pętla: bierzemy po kolei każdą linię pliku
        print(line, end='')                # linia ma już na końcu znak nowej linii, więc end='' nie dodaje drugiego
