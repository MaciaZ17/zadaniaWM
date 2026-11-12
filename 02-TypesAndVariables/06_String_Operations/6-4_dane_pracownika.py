###
# A program for printing detailed information.
# Indeksy w tekście "Mr. John May, born on 1998-02-16":
# M0 r1 .2 spacja3 | J4 o5 h6 n7 | spacja8 | M9 a10 y11 | ,12 spacja13 ... data od 22 do 31
#
employee = "Mr. John May, born on 1998-02-16"      # dane pracownika w jednym tekście
print(f'Name: {employee[4:8]}')                    # slicing [4:8] = znaki od indeksu 4 do 7 -> John
print(f'Surname: {employee[9:12]}')                # znaki od 9 do 11 -> May
print(f'Born: {employee[22:32]}')                  # znaki od 22 do 31 -> 1998-02-16
print(f'Initials: {employee[4]}{employee[9]}')     # pierwsza litera imienia i nazwiska -> JM
