###
# Functions to read any data type from the keyboard
#
def input_string(message):           # funkcja wczytuje napis; message to tekst pytania
    text = input(message)            # pokazujemy pytanie i czekamy na odpowiedź
    return text                      # oddajemy wpisany napis bez zmian

def input_integer(message):          # funkcja wczytuje liczbę całkowitą
    text = input(message)            # wczytujemy odpowiedź (to zawsze napis)
    return int(text)                 # zamieniamy napis na liczbę całkowitą i ją oddajemy

def input_real(message):             # funkcja wczytuje liczbę z częścią po kropce, np. 5250.50
    text = input(message)            # wczytujemy odpowiedź
    return float(text)               # zamieniamy napis na taką liczbę i ją oddajemy

def input_boolean(message):          # funkcja wczytuje odpowiedź tak/nie
    text = input(message)            # wczytujemy odpowiedź
    if text == 'y' or text == 'Y':   # jeśli wpisano y albo Y
        return True                  # oddajemy True, czyli tak
    else:                            # jeśli wpisano coś innego
        return False                 # oddajemy False, czyli nie
