###
# Sprawdzanie typów danych funkcją type().
#
print(type(50))                                  # 50 to liczba całkowita -> <class 'int'>
print(type(149.17))                              # liczba z kropką dziesiętną -> <class 'float'>
print(type(4 * 7))                               # int * int = int (28) -> <class 'int'>
print(type(4.0 * 7))                             # float * int = float (28.0) -> <class 'float'>
print(type("Krakow University of Economics"))    # tekst w cudzysłowie -> <class 'str'>
print(type(True))                                # wartość logiczna -> <class 'bool'>
print(type(2 > 5))                               # porównanie daje False, więc -> <class 'bool'>
