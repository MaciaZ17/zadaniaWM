###
# Returns True if the expression is a palindrome
#
def f(palindrome):                                  # funkcja sprawdza, czy napis czytany od tyłu jest taki sam
    reversed_text = ''                              # pusty napis, zbudujemy w nim napis od tyłu
    for char in palindrome:                         # pętla: bierzemy po kolei każdy znak
        reversed_text = char + reversed_text        # dokładamy znak na początek, więc kolejność się odwraca
    return palindrome == reversed_text              # porównanie daje True, gdy oba napisy są takie same

def main():                                         # program główny
    print('f("radar") returns', f("radar"))         # powinno wyjść True
    print('f("12-11-21") returns', f("12-11-21"))   # powinno wyjść True
    print('f("book") returns', f("book"))           # powinno wyjść False

if __name__ == "__main__":                          # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                          # wtedy uruchamiamy program główny
