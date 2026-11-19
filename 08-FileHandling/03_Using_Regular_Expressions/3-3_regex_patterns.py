###
# Regular expression patterns for the Regex101 task,
# tested in Python with re.findall()
#
# Te same wzorce wklejasz w regex101.com (bez r'' i bez cudzysłowów).
# Krótki słowniczek:
#   \d     jedna cyfra
#   \d+    jedna lub więcej cyfr
#   \d{4}  dokładnie 4 cyfry,  \d{1,3}  od 1 do 3 cyfr
#   [A-Z]  jedna wielka litera,  [a-z]+  jedna lub więcej małych liter
#   \b     granica słowa (początek albo koniec słowa)
import re                                                 # dołączamy moduł re do wyrażeń regularnych

text = ('Alice was born on March 12, 1992. Her brother, John, was born on June 5, 1988. '
        'They have a mutual friend named Mike, whose phone number is 555-123-4567. '
        'In their hometown, which has a population of 1,234 or 1,235 people, a holiday '
        'festival is held every year on December 25. Alice works in an office with 30 '
        'employees. Her phone number is 555-765-4321.')   # tekst z zadania (nawiasy pozwalają zapisać go w kilku linijkach)

dates = r'[A-Z][a-z]+ \d{1,2}, \d{4}'                     # data: słowo z wielkiej litery, spacja, 1-2 cyfry, przecinek, spacja, 4 cyfry
phones = r'\d{3}-\d{3}-\d{4}'                             # telefon: 3 cyfry, minus, 3 cyfry, minus, 4 cyfry
thousands = r'\d{1,3},\d{3}'                              # liczba z przecinkiem tysięcy: 1-3 cyfry, przecinek, 3 cyfry
names = r'\b[A-Z][a-z]+\b'                                # słowo zaczynające się wielką literą (łapie też np. March i Her)
numbers = r'\b\d+\b'                                      # ciągi cyfr; łapie też kawałki telefonów i dat

# r'...' to napis "surowy": Python nie zmienia w nim ukośników \, więc wzorzec zostaje taki, jak go wpisaliśmy.
print('Dates:', re.findall(dates, text))                  # findall() oddaje listę wszystkich pasujących fragmentów
print('Phone numbers:', re.findall(phones, text))         # wypisujemy telefony
print('Thousands:', re.findall(thousands, text))          # wypisujemy liczby z przecinkiem
print('Names:', re.findall(names, text))                  # wypisujemy słowa z wielkiej litery
print('Numbers:', re.findall(numbers, text))              # wypisujemy wszystkie liczby
