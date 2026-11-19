###
# Returns a string of n asterisks separated by a slash sign
#
def f(n):                           # funkcja robi napis z n gwiazdek oddzielonych ukośnikiem
    result = ''                     # pusty napis, będziemy do niego doklejać znaki
    for i in range(n):              # powtarzamy n razy (i to kolejne liczby 0, 1, 2...)
        if i > 0:                   # jeśli to nie pierwsza gwiazdka
            result = result + '/'   # doklejamy ukośnik
        result = result + '*'       # doklejamy gwiazdkę
    return result                   # funkcja oddaje gotowy napis

def main():                         # program główny
    print('f(4) returns', f(4))     # powinno wyjść */*/*/*
    print('f(1) returns', f(1))     # powinno wyjść *

if __name__ == "__main__":          # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                          # wtedy uruchamiamy program główny
