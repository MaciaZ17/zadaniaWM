###
# Returns numbers from 1 to n as a string
#
def f(n):                           # funkcja skleja liczby od 1 do n w jeden napis
    result = ''                     # pusty napis na start
    for i in range(1, n + 1):       # bierzemy liczby od 1 do n
        result = result + str(i)    # str() zamienia liczbę na napis, żeby dało się ją dokleić
    return result                   # funkcja oddaje gotowy napis

def main():                         # program główny
    print('f(11) returns', f(11))   # powinno wyjść 1234567891011
    print('f(4) returns', f(4))     # powinno wyjść 1234

if __name__ == "__main__":          # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                          # wtedy uruchamiamy program główny
