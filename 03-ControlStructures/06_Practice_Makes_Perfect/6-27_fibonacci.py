###
# Pierwsze 20 wyrazów ciągu Fibonacciego: 0 1 1 2 3 5 8 ...
#
previous = 0                                                 # pierwszy wyraz ciągu
current = 1                                                  # drugi wyraz ciągu
for i in range(20):                                          # wypiszemy 20 wyrazów
    print(previous, end=' ')                                 # wypisujemy aktualny wyraz
    next_number = previous + current                         # kolejny wyraz to suma dwóch poprzednich
    previous = current                                       # przesuwamy się: dotychczasowy drugi staje się pierwszym
    current = next_number                                    # a nowa suma staje się drugim
print()                                                      # nowa linia na końcu
