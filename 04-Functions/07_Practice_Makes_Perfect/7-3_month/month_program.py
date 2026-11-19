###
# Prints the name of a month based on its number
#
import months                                                        # dołączamy nasz plik months.py

def main():                                                          # program główny
    number = int(input('Enter month number: '))                      # wczytujemy numer miesiąca jako liczbę
    print('The name of month', number, 'is', months.month(number))   # funkcja month z pliku months daje nazwę, wypisujemy ją

if __name__ == "__main__":                                           # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                           # wtedy uruchamiamy program główny
