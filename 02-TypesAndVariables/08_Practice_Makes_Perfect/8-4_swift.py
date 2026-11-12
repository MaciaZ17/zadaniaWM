###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
# Testy: BPKOPLPW -> BPKO, PL ; CHASUS33 -> CHAS, US ; DEUTDEFF -> DEUT, DE
#
swift = input('Enter SWIFT code: ')                # wczytujemy kod SWIFT jako tekst
print(f'Bank Code: {swift[0:4]}')                  # pierwsze 4 znaki (indeksy 0-3) to kod banku
print(f'Country Code: {swift[4:6]}')               # kolejne 2 znaki (indeksy 4-5) to kod kraju
