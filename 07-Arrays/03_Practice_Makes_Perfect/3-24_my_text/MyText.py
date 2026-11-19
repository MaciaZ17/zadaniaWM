###
# Module with functions that operate on words in a text
#
def word_count(text):                                     # funkcja zwraca liczbę słów w tekście
    words = text.split()                                  # split() dzieli tekst na listę słów w miejscach spacji
    return len(words)                                     # liczba słów to liczba elementów listy

def words_by_length(text):                                # funkcja zwraca słowa od najdłuższego do najkrótszego
    words = text.split()                                  # dzielimy tekst na słowa
    n = len(words)                                        # liczba słów
    for i in range(n):                                    # sortowanie bąbelkowe: n przejść
        for j in range(n - i - 1):                        # porównujemy sąsiednie słowa
            if len(words[j]) < len(words[j + 1]):         # jeśli pierwsze jest krótsze od następnego
                temp = words[j]                           # zamieniamy je miejscami
                words[j] = words[j + 1]                   # na jego miejsce wstawiamy drugi
                words[j + 1] = temp                       # na miejsce drugiego wstawiamy zapamiętany
    return words                                          # funkcja oddaje posortowane słowa

def words_alphabetically(text):                           # funkcja zwraca słowa w kolejności alfabetycznej
    words = text.split()                                  # dzielimy tekst na słowa
    n = len(words)                                        # liczba słów
    for i in range(n):                                    # sortowanie bąbelkowe: n przejść
        for j in range(n - i - 1):                        # porównujemy sąsiednie słowa
            if words[j].lower() > words[j + 1].lower():   # lower() zmienia na małe litery, żeby An i a stały obok siebie
                temp = words[j]                           # zamieniamy je miejscami
                words[j] = words[j + 1]                   # na jego miejsce wstawiamy drugi
                words[j + 1] = temp                       # na miejsce drugiego wstawiamy zapamiętany
    return words                                          # funkcja oddaje posortowane słowa
