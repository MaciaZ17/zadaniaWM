###
# Checks if a number entered from the keyboard
# is within the range <2, 15>
#
import number_range                                              # dołączamy nasz plik number_range.py

def main():                                                      # program główny
    x = 2                                                        # początek przedziału
    y = 15                                                       # koniec przedziału
    number = int(input('A number: '))                            # wczytujemy liczbę
    if number_range.in_range(number, x, y):                      # jeśli funkcja oddała True
        answer = 'yes'                                           # odpowiedź: tak
    else:                                                        # jeśli oddała False
        answer = 'no'                                            # odpowiedź: nie
    print(f'Number {number} in the range <{x},{y}>: {answer}')   # wypisujemy wynik, np. Number 7 in the range <2,15>: yes

if __name__ == "__main__":                                       # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                       # wtedy uruchamiamy program główny
