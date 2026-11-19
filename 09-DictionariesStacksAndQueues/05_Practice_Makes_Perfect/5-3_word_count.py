###
# Counts how many times each word appears in a paragraph
#
paragraph = "cat dog mouse cat rat cat mouse"       # tekst z zadania

word_counts = {}                                    # pusty słownik: słowo będzie kluczem, liczba wystąpień wartością
for word in paragraph.split():                      # split() dzieli tekst na słowa; bierzemy je po kolei
    if word in word_counts:                         # jeśli słowo już jest w słowniku
        word_counts[word] = word_counts[word] + 1   # zwiększamy jego licznik o 1
    else:                                           # jeśli to pierwsze wystąpienie
        word_counts[word] = 1                       # dodajemy słowo z licznikiem 1

for word, count in word_counts.items():             # bierzemy po kolei każdą parę słowo : liczba
    print(word, ':', count)                         # wypisujemy, np. cat : 3
