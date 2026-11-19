###
# Returns the difference between the largest
# and the smallest number
#
def f(number1, number2, number3):               # funkcja liczy różnicę między największą a najmniejszą liczbą
    largest = max(number1, number2, number3)    # max() wybiera największą
    smallest = min(number1, number2, number3)   # min() wybiera najmniejszą
    return largest - smallest                   # funkcja oddaje różnicę

def main():                                     # program główny
    print('f(7, 4, 9) returns', f(7, 4, 9))     # powinno wyjść 5 (9 - 4)
    print('f(2, 12, 8) returns', f(2, 12, 8))   # powinno wyjść 10 (12 - 2)

if __name__ == "__main__":                      # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                      # wtedy uruchamiamy program główny
