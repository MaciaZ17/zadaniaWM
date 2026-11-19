###
# Copies the book data from each genre to its corresponding file
#
import csv                                                            # moduł do plików CSV

def read_books(file_name):                                            # funkcja wczytuje książki z pliku CSV i oddaje listę wierszy
    books = []                                                        # pusta lista na książki
    with open(file_name, 'r', newline='') as file:                    # otwieramy plik do odczytu
        reader = csv.reader(file)                                     # każdą linię dostaniemy jako listę kolumn
        for row in reader:                                            # bierzemy po kolei każdy wiersz
            books.append(row)                                         # dopisujemy go do listy
    return books                                                      # funkcja oddaje wszystkie wiersze

def books_of_genre(books, genre):                                     # funkcja wybiera książki z danego gatunku
    selected = []                                                     # pusta lista na wybrane książki
    for book in books:                                                # bierzemy po kolei każdą książkę
        if genre in book:                                             # jeśli któraś kolumna jest równa nazwie gatunku
            selected.append(book)                                     # dopisujemy książkę do wybranych
    return selected                                                   # funkcja oddaje wybrane książki

def save_books(books, file_name):                                     # funkcja zapisuje książki do pliku
    with open(file_name, 'w') as file:                                # otwieramy plik do zapisu
        for book in books:                                            # bierzemy po kolei każdą książkę
            file.write(','.join(book) + '\n')                         # ','.join() skleja kolumny przecinkami; dodajemy nową linię

def main():                                                           # program główny
    books = read_books('books.csv')                                   # wczytujemy wszystkie książki
    genres = ['Fantasy', 'Historical', 'Romance', 'Classic']          # lista gatunków
    for genre in genres:                                              # bierzemy po kolei każdy gatunek
        file_name = 'books_' + genre.lower() + '.txt'                 # nazwa pliku, np. books_fantasy.txt (lower() zmienia na małe litery)
        selected = books_of_genre(books, genre)                       # wybieramy książki z tego gatunku
        save_books(selected, file_name)                               # zapisujemy je do pliku
        print(genre, '-->', file_name, '(' + str(len(selected)) + ' books)')  # informujemy, co zapisaliśmy

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
