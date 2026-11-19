###
# Returns True if at least one of the numbers is negative
#
def f(n1, n2, n3):                                # funkcja sprawdza, czy któraś z trzech liczb jest ujemna
    if n1 < 0 or n2 < 0 or n3 < 0:                # or znaczy "lub": wystarczy, że jedna liczba jest ujemna
        return True                               # oddajemy True, czyli tak
    else:                                         # w przeciwnym razie
        return False                              # oddajemy False, czyli nie

def main():                                       # program główny
    print('f(11, 6, -4) returns', f(11, 6, -4))   # powinno wyjść True
    print('f(5, 4, 14) returns', f(5, 4, 14))     # powinno wyjść False

if __name__ == "__main__":                        # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                        # wtedy uruchamiamy program główny
