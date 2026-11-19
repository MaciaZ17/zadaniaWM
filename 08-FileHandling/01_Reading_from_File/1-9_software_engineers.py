###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'                      # plik z pracownikami (w szablonie jest .txt, w treści zadania .csv)

# Position
job_title = 'Software Engineer'                   # stanowisko, którego szukamy

counter = 1                                       # numer na liście, zaczynamy od 1
with open(file_name, 'r') as file:                # otwieramy plik do odczytu
    for line in file:                             # pętla: bierzemy po kolei każdą linię
        if job_title in line:                     # in sprawdza, czy napis Software Engineer jest w tej linii
            print(f'{counter}. {line.strip()}')   # strip() usuwa znak nowej linii z końca
            counter = counter + 1                 # następny pracownik dostanie kolejny numer
