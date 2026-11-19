###
# Calculates RPN (Reverse Polish Notation) expressions using a stack
#
# W RPN najpierw podajemy liczby, potem działanie: 2 3 + znaczy 2 + 3.
# Każdy element wpisujesz osobno i zatwierdzasz Enterem, np.: 2, 3, +, =
import queue                                                        # moduł z gotowym stosem

stack = queue.LifoQueue()                                           # pusty stos na liczby
operators = ['+', '-', '*', '/']                                    # dozwolone działania

while True:                                                         # pętla działa, dopóki nie wpiszemy q
    value = input('Number, operator (+ - * /), = or q to quit: ')   # wczytujemy jeden element
    if value == 'q':                                                # jeśli wpisano q
        break                                                       # kończymy program
    elif value in operators:                                        # jeśli to działanie
        if stack.qsize() < 2:                                       # do działania potrzebne są 2 liczby na stosie
            print('Not enough numbers on the stack.')               # informujemy o błędzie
            continue                                                # continue wraca na początek pętli
        b = stack.get()                                             # zdejmujemy górną liczbę (to druga liczba działania)
        a = stack.get()                                             # zdejmujemy następną (to pierwsza liczba działania)
        if value == '+':                                            # dodawanie
            stack.put(a + b)                                        # wynik kładziemy z powrotem na stos
        elif value == '-':                                          # odejmowanie
            stack.put(a - b)                                        # wynik kładziemy na stos
        elif value == '*':                                          # mnożenie
            stack.put(a * b)                                        # wynik kładziemy na stos
        elif value == '/':                                          # dzielenie
            stack.put(a / b)                                        # wynik kładziemy na stos
    elif value == '=':                                              # znak równości kończy wyrażenie
        if stack.empty():                                           # jeśli stos jest pusty
            print('Nothing to calculate.')                          # nie ma wyniku
        else:                                                       # w przeciwnym razie
            print('Result:', stack.get())                           # zdejmujemy i wypisujemy wynik
    else:                                                           # wszystko inne traktujemy jak liczbę
        try:                                                        # próbujemy zamienić napis na liczbę
            stack.put(float(value))                                 # jeśli się uda, kładziemy liczbę na stos
        except ValueError:                                          # jeśli to nie liczba (np. litera)
            print('Wrong value:', value)                            # informujemy o błędzie
