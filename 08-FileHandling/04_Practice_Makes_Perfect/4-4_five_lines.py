###
# Displays a file five lines at a time,
# waiting for the Enter key after each part
#
file_name = 'it_company.csv'            # plik do wyświetlenia

with open(file_name, 'r') as file:      # otwieramy plik do odczytu
    lines = file.read().splitlines()    # wczytujemy cały plik i dzielimy go na listę linii

i = 0                                   # i to numer linii, zaczynamy od 0
while i < len(lines):                   # powtarzamy, dopóki są linie do wypisania
    print(lines[i])                     # wypisujemy linię
    i = i + 1                           # przechodzimy do następnej
    if i % 5 == 0 and i < len(lines):   # co 5 linii (gdy reszta z dzielenia przez 5 to 0), o ile coś jeszcze zostało
        input('Press Enter key...')     # input() czeka, aż naciśniesz Enter
