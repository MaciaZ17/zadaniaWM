###
# Analiza losowania liczby z zakresu 5-10. Uruchom program 5 razy - za każdym razem
# wynik może być inny (liczba całkowita od 5 do 10 włącznie).
#
import random                                      # moduł z generatorem liczb losowych
random_number = random.randint(5,10)               # losujemy liczbę całkowitą z przedziału <5,10>
print(random_number)                               # wypisujemy wylosowaną liczbę
