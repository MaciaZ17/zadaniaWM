###
# Returns the given text with all characters
# separated by a dash sign
#
def f(text):                                            # funkcja wstawia myślnik między wszystkie znaki
    result = ''                                         # pusty napis na wynik
    for i in range(len(text)):                          # i to numer kolejnego znaku: 0, 1, 2...
        if i > 0:                                       # jeśli to nie pierwszy znak
            result = result + '-'                       # doklejamy myślnik
        result = result + text[i]                       # doklejamy znak o numerze i
    return result                                       # funkcja oddaje wynik

def main():                                             # program główny
    print('f("University") returns', f("University"))   # powinno wyjść U-n-i-v-e-r-s-i-t-y
    print('f("UE") returns', f("UE"))                   # powinno wyjść U-E
    print('f("x") returns', f("x"))                     # powinno wyjść x
    print('f("") returns', f(""))                       # powinno wyjść pusty napis

if __name__ == "__main__":                              # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                              # wtedy uruchamiamy program główny
