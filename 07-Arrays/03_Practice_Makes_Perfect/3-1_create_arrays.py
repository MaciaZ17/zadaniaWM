###
# Creates different arrays and prints their content
#
import random                                                         # dołączamy moduł random, bo niektóre listy mają losowe liczby

# Zapis [wartość for i in range(n)] tworzy listę z n elementów:
# dla każdego i z range wstawia do listy podaną wartość.
arr1 = [3, 7, 1, 0, 4]                                                # zwykła lista pięciu liczb
arr2 = [[2, 3], [7, 1], [0, 4]]                                       # lista list: 3 wiersze po 2 liczby
arr3 = [7 for i in range(5)]                                          # 5 razy liczba 7: [7, 7, 7, 7, 7]
arr4 = [i for i in range(1, 10)]                                      # liczby od 1 do 9
arr5 = [i * 2 for i in range(1, 10)]                                  # każda liczba od 1 do 9 razy 2: 2, 4, ... 18
arr6 = [random.randint(1, 20) for i in range(10)]                     # 10 losowych liczb od 1 do 20
arr7 = [[] for i in range(5)]                                         # 5 pustych list
arr8 = [[1 for i in range(2)] for j in range(4)]                      # 4 wiersze, w każdym 2 jedynki
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]  # 5 wierszy po 3 losowe liczby

arr10 = [4, 0, 3]                                                     # lista z wartościami 4, 0, 3
arr11 = [0 for i in range(15)]                                        # 15 zer
arr12 = [i for i in range(1, 31)]                                     # liczby od 1 do 30 (31 nie wchodzi)
arr13 = [random.randint(0, 1) for i in range(20)]                     # 20 losowych wartości 0 albo 1
arr14 = [[False for i in range(2)] for j in range(5)]                 # 5 wierszy, 2 kolumny, wszędzie False

print('arr1:', arr1)                                                  # wypisujemy arr1
print('arr2:', arr2)                                                  # wypisujemy arr2
print('arr3:', arr3)                                                  # wypisujemy arr3
print('arr4:', arr4)                                                  # wypisujemy arr4
print('arr5:', arr5)                                                  # wypisujemy arr5
print('arr6:', arr6)                                                  # wypisujemy arr6
print('arr7:', arr7)                                                  # wypisujemy arr7
print('arr8:', arr8)                                                  # wypisujemy arr8
print('arr9:', arr9)                                                  # wypisujemy arr9
print('arr10:', arr10)                                                # wypisujemy arr10
print('arr11:', arr11)                                                # wypisujemy arr11
print('arr12:', arr12)                                                # wypisujemy arr12
print('arr13:', arr13)                                                # wypisujemy arr13
print('arr14:', arr14)                                                # wypisujemy arr14
