###
# Converts a natural number to a binary number using a stack
#
import queue                                        # moduł z gotowym stosem

number = int(input('Natural number: '))             # wczytujemy liczbę
stack = queue.LifoQueue()                           # pusty stos na reszty z dzielenia

print('Division', '\t', 'Remainder')                # nagłówek tabeli; \t to tabulator (odstęp)
n = number                                          # kopia liczby, którą będziemy dzielić
while n > 0:                                        # dzielimy, dopóki liczba nie spadnie do zera
    remainder = n % 2                               # reszta z dzielenia przez 2 (0 albo 1)
    print(f'{n} / 2 = {n // 2}', '\t', remainder)   # wypisujemy wiersz tabeli, np. 18 / 2 = 9   0
    stack.put(remainder)                            # kładziemy resztę na stos
    n = n // 2                                      # dzielimy liczbę przez 2 (bez reszty)

binary = ''                                         # pusty napis na wynik
while not stack.empty():                            # zdejmujemy reszty, dopóki stos nie jest pusty
    binary = binary + str(stack.get())              # ostatnia reszta wychodzi pierwsza, więc cyfry są w dobrej kolejności
if binary == '':                                    # dla liczby 0 pętla się nie wykonała
    binary = '0'                                    # więc wynik to 0

print('Natural number:', number)                    # wypisujemy liczbę
print('Binary number:', binary)                     # i jej zapis dwójkowy (dla 18: 10010)
