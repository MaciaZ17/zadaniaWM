###
# Returns a sentence with spaces removed
#
def f(sentence):                                                      # funkcja usuwa spacje ze zdania
    result = ''                                                       # pusty napis na wynik
    for char in sentence:                                             # pętla: bierzemy po kolei każdy znak
        if char != ' ':                                               # jeśli znak nie jest spacją
            result = result + char                                    # doklejamy go do wyniku
    return result                                                     # funkcja oddaje zdanie bez spacji

def main():                                                           # program główny
    print(f("integrated development environment"))                    # powinno wyjść integrateddevelopmentenvironment
    print(f("A programming language is a system of notation for writing computer programs"))  # drugi przykład z zadania

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
