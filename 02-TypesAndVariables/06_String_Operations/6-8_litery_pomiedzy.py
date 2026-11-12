###
# Ile liter znajduje się pomiędzy dwiema podanymi literami.
# Testy: A i D -> 2, B i M -> 10, K i K -> 0
#
first = input('Enter first letter: ')              # wczytujemy pierwszą literę
last = input('Enter last letter: ')                # wczytujemy drugą literę
first_letter_code = ord(first)                     # kod pierwszej litery
last_letter_code = ord(last)                       # kod drugiej litery
number_of_letters = last_letter_code - first_letter_code - 1   # litery między: różnica kodów minus 1 (bez końców)
number_of_letters = max(0, number_of_letters)      # dla K i K wychodzi -1, a ma być 0; max(0, ...) nie pozwala zejść poniżej 0
print(f'Between {first} and {last} is {number_of_letters} letters')   # wypisujemy wynik
