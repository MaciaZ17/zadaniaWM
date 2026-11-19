###
# Example: the if __name__ == "__main__" construct
# together with the main() function
#
def add(a, b):                             # funkcja dodaje dwie liczby
    return a + b                           # oddaje ich sumę

def subtract(a, b):                        # funkcja odejmuje dwie liczby
    return a - b                           # oddaje ich różnicę

def main():                                # funkcja main to nasz program główny
    x = 10                                 # pierwsza liczba
    y = 5                                  # druga liczba
    print(f"Add: {add(x, y)}")             # w {} wstawiamy wynik dodawania (15)
    print(f"Subtract: {subtract(x, y)}")   # w {} wstawiamy wynik odejmowania (5)

# Gdy ten plik jest dołączony do innego przez import, warunek poniżej jest fałszywy
# i main() się nie uruchomi. Dzięki temu import nie odpala programu.
if __name__ == "__main__":                 # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                 # wtedy uruchamiamy program główny
