###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Anna'                                      # imię (zamień na swoje)
surname = 'May'                                    # nazwisko (zamień na swoje)
characters_in_name = len(name)                     # len() zwraca liczbę znaków w tekście
print(f'Your name has {characters_in_name} characters')            # liczba znaków imienia
print(f'Your surname has {len(surname)} characters')              # liczba znaków nazwiska
print(f'Your full name has {len(name + " " + surname)} characters')  # łączymy imię + spacja + nazwisko i liczymy znaki
