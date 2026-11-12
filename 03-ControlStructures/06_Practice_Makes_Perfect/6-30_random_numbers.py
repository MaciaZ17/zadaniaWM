###
# 20 losowych liczb całkowitych z zakresu 5-10
#
import random                                                # moduł do losowania
for i in range(20):                                          # powtarzamy 20 razy
    print(random.randint(5, 10), end=' ')                    # losujemy liczbę 5..10 włącznie i wypisujemy w jednej linii
print()                                                      # nowa linia na końcu
