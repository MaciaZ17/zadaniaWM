###
# Populacja świata: liczba ludzi i procent na półkuli północnej i południowej.
#
total = 8000000000                                 # cała populacja świata
north = 7200000000                                 # ludność półkuli północnej
south = total - north                              # półkula południowa = reszta (800 000 000)
print("World population: ", total)                 # wypisujemy całą populację
print("Northern Hemisphere: ", north)              # liczba ludzi na północy
print("Northern Hemisphere in %: ", north/total*100)   # procent na północy (90.0)
print("Southern Hemisphere: ", south)              # liczba ludzi na południu
print("Southern Hemisphere in %: ", south/total*100)   # procent na południu (10.0)
