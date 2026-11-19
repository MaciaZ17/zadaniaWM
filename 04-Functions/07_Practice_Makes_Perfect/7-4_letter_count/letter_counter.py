###
# Module with a function that counts how many times
# the given letter appears in a text
#
# Małe e i duże E to dla Pythona różne znaki.
def count_letter(text, letter):     # funkcja liczy, ile razy litera jest w tekście
    counter = 0                     # licznik, na początku 0
    for char in text:               # pętla: bierzemy po kolei każdy znak tekstu
        if char == letter:          # jeśli znak to szukana litera
            counter = counter + 1   # zwiększamy licznik o 1
    return counter                  # funkcja oddaje wynik
