###
# Returns the sum of repeated digits in a number
#
def f(number):                                    # funkcja sumuje cyfry, które w liczbie powtarzają się
    digits = str(number)                          # zamieniamy liczbę na napis, żeby brać cyfry po kolei
    total = 0                                     # suma, na początku 0
    for char in digits:                           # pętla: bierzemy po kolei każdą cyfrę
        if digits.count(char) > 1:                # count() mówi, ile razy cyfra jest w liczbie; więcej niż 1 to powtórka
            total = total + int(char)             # dodajemy tę cyfrę do sumy
    return total                                  # funkcja oddaje sumę

def main():                                       # program główny
    print('f(1027) returns', f(1027))             # powinno wyjść 0 (nic się nie powtarza)
    print('f(230335) returns', f(230335))         # powinno wyjść 9 (3 + 3 + 3)
    print('f(513553007) returns', f(513553007))   # powinno wyjść 21 (5+5+5 + 3+3 + 0+0)

if __name__ == "__main__":                        # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                        # wtedy uruchamiamy program główny
