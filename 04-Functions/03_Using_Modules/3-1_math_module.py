###
# To use the functions available in an external module,
# you must include that module in your program.
import math                                         # dołączamy moduł math, czyli gotowy zestaw funkcji matematycznych

square_root = math.sqrt(7)                          # math.sqrt() liczy pierwiastek kwadratowy
print('A square root of 7 is', square_root)         # wypisujemy wynik

natural_log = math.log(5)                           # math.log() liczy logarytm naturalny
print('A natural logarithm of 5 is', natural_log)   # wypisujemy wynik

angle_radians = math.radians(90)                    # Python liczy kąty w radianach, więc zamieniamy 90 stopni na radiany
sine_90 = math.sin(angle_radians)                   # math.sin() liczy sinus kąta
print('A sine of 90 degrees is', sine_90)           # wypisujemy wynik (1.0)
