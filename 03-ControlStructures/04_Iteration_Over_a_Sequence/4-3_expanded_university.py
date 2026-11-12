###
# Prints the name of university where you are studying
# with an extra space between characters, e.g. 'book' -> 'b o o k'
#
university = 'Krakow University of Economics'                # oryginalna nazwa uczelni
university_expanded = ''                                     # pusty tekst, do którego będziemy dopisywać znaki

for char in university:                                      # bierzemy po kolei każdy znak
    university_expanded = university_expanded + char + ' '   # dopisujemy znak i za nim spację

print(university)                                            # oryginalna nazwa
print(university_expanded)                                   # nazwa z odstępami
