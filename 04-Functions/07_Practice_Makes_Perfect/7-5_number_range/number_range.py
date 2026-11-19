###
# Module with a function that checks if a number
# is within the range <x, y>
#
def in_range(number, x, y):           # funkcja sprawdza, czy liczba jest między x a y (x i y też się liczą)
    if number >= x and number <= y:   # jeśli liczba jest nie mniejsza niż x i nie większa niż y
        return True                   # oddajemy True, czyli tak
    else:                             # w przeciwnym razie
        return False                  # oddajemy False, czyli nie
