###
# Program for testing built-in functions
#
max_number = max(7, 5, 6, 3, 8, 2)                                    # max() wybiera największą liczbę, zapisujemy ją w zmiennej
print('Max number of 7,5,6,3,8,2 is', max_number)                     # wypisujemy tekst, a po nim wynik (8)

min_number = min(4, 7, 2, 3, 9, 8)                                    # min() wybiera najmniejszą liczbę
print('Min number of 4,7,2,3,9,8 is', min_number)                     # wypisujemy wynik (2)

str_length = len("computer science")                                  # len() liczy znaki w napisie, spacja też się liczy
print('The number of characters in "computer science" is', str_length)  # wypisujemy wynik (16)

letter = input('Enter a letter: ')                                    # input() czeka, aż coś wpiszesz i naciśniesz Enter
print('The letter read from the keyboard is', letter)                 # wypisujemy literę, którą wpisałeś

number = int("20303")                                                 # int() zamienia napis "20303" na liczbę, na której można liczyć
print('The number representing the string "20303" is', number)        # wypisujemy liczbę
print('Type before:', type("20303"), 'type after:', type(number))     # type() pokazuje rodzaj danych: str to napis, int to liczba

binary_string = bin(304)                                              # bin() zapisuje liczbę w systemie dwójkowym (same 0 i 1)
print('Binary string representing 304 is', binary_string)             # wynik: 0b100110000 (0b oznacza liczbę dwójkową)

hex_string = hex(304)                                                 # hex() zapisuje liczbę w systemie szesnastkowym
print('Hexadecimal string representing 304 is', hex_string)           # wynik: 0x130 (0x oznacza liczbę szesnastkową)

euro_code = ord('€')                                                  # ord() podaje numer znaku w tabeli Unicode (każdy znak ma swój numer)
print('The Unicode code of the € sign is', euro_code)                 # wynik: 8364

absolute_value = abs(-17)                                             # abs() usuwa minus z liczby
print('The absolute value of -17 is', absolute_value)                 # wynik: 17
