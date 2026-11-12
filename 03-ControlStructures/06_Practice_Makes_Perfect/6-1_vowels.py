###
# vowels.py - liczy samogłoski w tekście (wersja z pętlą while zamiast for)
# UWAGA: nie miałem Twojego oryginalnego vowels.py, więc napisałem własną wersję.
# Wersja z for wyglądałaby tak:
#   for char in text:
#       if char in vowels:
#           count += 1
#
text = input('Enter text: ')                                 # wczytujemy tekst
vowels = 'aeiouAEIOU'                                        # lista samogłosek (małe i wielkie litery)
count = 0                                                    # licznik samogłosek
i = 0                                                        # indeks aktualnego znaku (ręczny licznik pętli while)

while i < len(text):                                         # dopóki indeks mieści się w tekście
    char = text[i]                                           # pobieramy znak o indeksie i
    if char in vowels:                                       # czy znak występuje w tekście z samogłoskami
        count += 1                                           # zwiększamy licznik samogłosek
    i += 1                                                   # przechodzimy do następnego znaku

print(f'Number of vowels: {count}')                          # wypisujemy wynik
