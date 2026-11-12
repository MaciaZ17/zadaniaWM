###
# String manipulation
#
movie = "The Lord of the Rings: The Return of the King"   # tytuł filmu

# print number of characters
print('Number of characters: ', len(movie))        # len() - liczba wszystkich znaków (ze spacjami)

# print title in capital letters
print(movie.upper())                               # upper() - zamienia wszystkie litery na wielkie

# print title in small letters
print(movie.lower())                               # lower() - zamienia wszystkie litery na małe

# print how many times the vowel "e" appears in the title
print('Letter e appears:', movie.count("e"))       # count() - zlicza wystąpienia (wynik: 5; liczy tylko małe "e")

# print where in the text is the word "Lord"
print('Lord is at index:', movie.find("Lord"))     # find() - indeks początku słowa (wynik: 4)

# print where in the text is the word "dragon"
print('dragon is at index:', movie.find("dragon")) # find() zwraca -1, gdy nic nie znajdzie
