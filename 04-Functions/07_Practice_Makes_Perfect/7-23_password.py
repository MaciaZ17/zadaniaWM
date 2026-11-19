###
# Returns True if the password has at least six characters
# and each character appears only once
#
def f(password):                                    # funkcja sprawdza, czy hasło jest poprawne
    if len(password) < 6:                           # jeśli hasło ma mniej niż 6 znaków
        return False                                # jest złe
    for char in password:                           # pętla: bierzemy po kolei każdy znak
        if password.count(char) > 1:                # jeśli znak występuje więcej niż raz
            return False                            # hasło jest złe
    return True                                     # hasło jest dobre

def main():                                         # program główny
    print('f("ax15") returns', f("ax15"))           # powinno wyjść False (za krótkie)
    print('f("book123") returns', f("book123"))     # powinno wyjść False (dwa razy o)
    print('f("A2water3") returns', f("A2water3"))   # powinno wyjść True (A i a to różne znaki)
    print('f("qwerty") returns', f("qwerty"))       # powinno wyjść True
    print('f("") returns', f(""))                   # powinno wyjść False (puste)

if __name__ == "__main__":                          # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                          # wtedy uruchamiamy program główny
