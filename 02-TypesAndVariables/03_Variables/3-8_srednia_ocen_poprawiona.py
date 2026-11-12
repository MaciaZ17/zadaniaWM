###
# A program that calculates and prints
# the average grade of a student  (WERSJA POPRAWIONA)
#
# Błędy w oryginale:
# 1) history = '3' było tekstem (str), a do liczenia potrzebna jest liczba -> history = 3
# 2) w wyrażeniu użyto nieistniejących nazw: mat, Art, muzic (Python odróżnia wielkie/małe litery
#    i wymaga dokładnie takiej samej nazwy jak przy tworzeniu zmiennej)
# 3) użyto minusa zamiast plusa przy muzyce
# 4) brak nawiasów: / 4 dzieliło tylko ostatni składnik, a nie całą sumę
# 5) w print był cudzysłów " zamknięty apostrofem ' (niezgodne znaki)
# 6) zmienna averege była błędnie napisana (poprawnie: average)
#
math = 5                                           # ocena z matematyki
art = 4                                            # ocena z plastyki
music = 5                                          # ocena z muzyki
history = 3                                        # ocena z historii (liczba, nie tekst!)
average = (math + art + music + history) / 4       # nawias: najpierw suma ocen, potem dzielenie przez 4 przedmioty
print("Average grade is", average)                 # wypisujemy średnią (4.25)
