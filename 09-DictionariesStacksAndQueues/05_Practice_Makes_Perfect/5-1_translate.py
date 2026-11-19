###
# Translates words from English to Polish
#
translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}                                               # słownik: angielskie słowo to klucz, polskie to wartość

word = input('Enter a word in English: ')       # wczytujemy słowo
word = word.lower()                             # lower() zmienia na małe litery, więc Mouse też zadziała
if word in translations:                        # in sprawdza, czy taki klucz jest w słowniku
    print('Translation:', translations[word])   # wypisujemy tłumaczenie
else:                                           # jeśli słowa nie ma w słowniku
    print('Translation is unavailable.')        # informujemy, że nie ma tłumaczenia
