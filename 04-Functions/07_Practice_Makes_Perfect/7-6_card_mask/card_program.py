###
# Masks some credit card digits and prints the card number
#
import card                            # dołączamy nasz plik card.py

def main():                            # program główny
    card_number = '5290312400019022'   # numer karty zapisany jako napis
    masked = card.hide(card_number)    # ukrywamy środek numeru
    print('Card number:', masked)      # wypisujemy wynik: 52**********9022

if __name__ == "__main__":             # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                             # wtedy uruchamiamy program główny
