###
# Reverses a text using a stack
#
import queue                                 # moduł z gotowym stosem (LifoQueue)

def reverse_text(text):                      # funkcja odwraca napis za pomocą stosu
    stack = queue.LifoQueue()                # pusty stos
    for char in text:                        # bierzemy po kolei każdy znak
        stack.put(char)                      # kładziemy go na stos
    result = ''                              # pusty napis na wynik
    while not stack.empty():                 # zdejmujemy znaki, dopóki stos nie jest pusty
        result = result + stack.get()        # ostatni znak wychodzi pierwszy, więc napis się odwraca
    return result                            # funkcja oddaje odwrócony napis

def main():                                  # program główny
    text = input('Enter text: ')             # wczytujemy tekst, np. Wiktor
    print('Reversed:', reverse_text(text))   # wypisujemy go od tyłu, np. rotkiW

if __name__ == "__main__":                   # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                   # wtedy uruchamiamy program główny
