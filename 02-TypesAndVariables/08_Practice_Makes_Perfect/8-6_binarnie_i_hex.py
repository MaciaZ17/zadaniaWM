###
# Zamiana liczby dziesiętnej na zapis binarny i szesnastkowy.
# Przykład: 125 -> 0b1111101, 0x7d
#
number = int(input('Enter number: '))              # wczytujemy liczbę całkowitą
print(f'Binary number: {bin(number)}')             # bin() zwraca tekst z zapisem dwójkowym (prefiks 0b)
print(f'Hexadecimal number: {hex(number)}')        # hex() zwraca tekst z zapisem szesnastkowym (prefiks 0x)
