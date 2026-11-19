###
# Checks if the brackets (), {}, [] are used correctly
#
import queue                                           # moduł z gotowym stosem (LifoQueue)

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"              # nawiasy poprawne
expression2 = "[(2+3]/4)"                              # nawiasy niepoprawne
expression3 = "(2-3*4+(5/6)"                           # nawiasy niepoprawne

def brackets_ok(expression):                           # funkcja sprawdza nawiasy; oddaje True albo False
    stack = queue.LifoQueue()                          # pusty stos na nawiasy otwierające
    for char in expression:                            # bierzemy po kolei każdy znak
        if char in '([{':                              # jeśli to nawias otwierający
            stack.put(char)                            # kładziemy go na stos
        elif char in ')]}':                            # jeśli to nawias zamykający
            if stack.empty():                          # a stos jest pusty, to nie ma czego zamknąć
                return False                           # błąd
            top = stack.get()                          # zdejmujemy ostatni nawias otwierający
            if char == ')' and top != '(':             # ) musi zamykać (
                return False                           # nawiasy do siebie nie pasują
            if char == ']' and top != '[':             # ] musi zamykać [
                return False                           # nawiasy do siebie nie pasują
            if char == '}' and top != '{':             # } musi zamykać {
                return False                           # nawiasy do siebie nie pasują
    return stack.empty()                               # na końcu stos musi być pusty; jeśli coś zostało, jakiś nawias nie został zamknięty

def check(expression):                                 # funkcja wypisuje wynik sprawdzenia
    if brackets_ok(expression):                        # jeśli nawiasy są poprawne
        print(expression, '-> brackets ok')            # wypisujemy ok
    else:                                              # w przeciwnym razie
        print(expression, '-> brackets not correct')   # wypisujemy błąd

def main():                                            # program główny
    check(expression1)                                 # sprawdzamy pierwsze wyrażenie
    check(expression2)                                 # drugie
    check(expression3)                                 # trzecie

if __name__ == "__main__":                             # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                             # wtedy uruchamiamy program główny
