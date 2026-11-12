###
# Kody liczbowe znaków. ord() zamienia znak na jego numer.
# UWAGA: w oryginale było f'a {ord('a')}' - te same apostrofy w środku i na zewnątrz
# powodują błąd w starszych wersjach Pythona, dlatego wewnątrz używam cudzysłowów.
#
print(f"a {ord('a')}")                             # 97
print(f"b {ord('b')}")                             # 98
print(f"z {ord('z')}")                             # 122
print(f"A {ord('A')}")                             # 65 (wielkie litery mają inne kody niż małe)
print(f"B {ord('B')}")                             # 66
print(f"Z {ord('Z')}")                             # 90
print(f"1 {ord('1')}")                             # 49 (to znak cyfry, nie liczba 1)
print(f"= {ord('=')}")                             # 61
print(f"+ {ord('+')}")                             # 43
print(f"€ {ord('€')}")                             # 8364
