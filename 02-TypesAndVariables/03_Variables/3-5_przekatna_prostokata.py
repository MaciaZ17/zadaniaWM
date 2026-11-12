###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math                                        # importujemy moduł math, bo zawiera funkcję sqrt (pierwiastek)
a = 5                                              # pierwszy bok prostokąta
b = 8                                              # drugi bok prostokąta
diagonal = math.sqrt(a**2 + b**2)                  # z twierdzenia Pitagorasa: przekątna = pierwiastek z (a^2 + b^2)
print("Diagonal:", diagonal)                       # wypisujemy długość przekątnej (ok. 9.43)
