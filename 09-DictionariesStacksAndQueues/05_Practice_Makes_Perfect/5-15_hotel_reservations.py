###
# Prints a summary of hotel reservations from a JSON file
#
import json                                                           # moduł do plików JSON

def read_reservations(file_name):                                     # funkcja wczytuje rezerwacje z pliku JSON
    with open(file_name, 'r', encoding='utf-8') as file:              # otwieramy plik do odczytu
        return json.load(file)                                        # oddajemy listę rezerwacji

def count_paid(reservations, paid):                                   # funkcja liczy rezerwacje opłacone (paid=True) albo nieopłacone (paid=False)
    count = 0                                                         # licznik, na początku 0
    for reservation in reservations:                                  # bierzemy po kolei każdą rezerwację
        if reservation['paid'] == paid:                               # jeśli ma szukany stan płatności
            count = count + 1                                         # zwiększamy licznik
    return count                                                      # funkcja oddaje wynik

def total_value(reservations, paid):                                  # funkcja sumuje ceny rezerwacji opłaconych albo nieopłaconych
    total = 0                                                         # suma, na początku 0
    for reservation in reservations:                                  # bierzemy po kolei każdą rezerwację
        if reservation['paid'] == paid:                               # jeśli ma szukany stan płatności
            total = total + reservation['price']                      # dodajemy jej cenę
    return total                                                      # funkcja oddaje sumę

def main():                                                           # program główny
    reservations = read_reservations('reservations.json')             # wczytujemy rezerwacje
    print('RESERVATIONS SUMMARY')                                     # nagłówek
    print('Number of rooms:', len(reservations))                      # liczba zarezerwowanych pokoi
    print('Paid reservations:', count_paid(reservations, True))       # liczba opłaconych
    print('Unpaid reservations:', count_paid(reservations, False))    # liczba nieopłaconych
    print('Total value of paid reservations:', total_value(reservations, True))  # suma opłaconych
    print('Total value of unpaid reservations:', total_value(reservations, False))  # suma nieopłaconych

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
