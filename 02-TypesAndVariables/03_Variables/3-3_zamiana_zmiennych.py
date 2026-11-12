###
# A program for swapping two variable values
# (Program zamienia wartości dwóch zmiennych miejscami.)
#
x = 7                                              # początkowa wartość x
y = 34                                             # początkowa wartość y
z = 0                                              # zmienna pomocnicza (auxiliary), tymczasowo przechowa jedną wartość
print("Before swapping: x=", x, "y=", y)           # wypisujemy wartości przed zamianą

# swap the values
z = x                                              # zapamiętujemy x w z (inaczej straciłbym 7 po następnej linii)
x = y                                              # do x wpisujemy starą wartość y (34)
y = z                                              # do y wpisujemy zapamiętaną starą wartość x (7)

print("After swapping: x=", x, "y=", y)            # wypisujemy wartości po zamianie (x=34, y=7)
