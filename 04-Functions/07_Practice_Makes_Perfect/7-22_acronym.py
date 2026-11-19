###
# Returns the acronym (first letters of all words)
#
def f(name):                                                          # funkcja robi skrót z pierwszych liter słów
    result = ''                                                       # pusty napis na skrót
    words = name.split()                                              # split() dzieli tekst na słowa w miejscach spacji
    for word in words:                                                # pętla: bierzemy po kolei każde słowo
        result = result + word[0]                                     # word[0] to pierwsza litera słowa; doklejamy ją
    return result                                                     # funkcja oddaje skrót

def main():                                                           # program główny
    print('f("Internet of Things") returns', f("Internet of Things"))  # powinno wyjść IoT
    print('f("For Your Information") returns', f("For Your Information"))  # powinno wyjść FYI
    print('f("Python") returns', f("Python"))                         # powinno wyjść P

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
