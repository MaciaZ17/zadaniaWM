###
# A program that prints a university abbreviation
#
university = "Krakow University of Economics"      # pełna nazwa uczelni
# Indeksy: "Krakow" = 0-5, spacja = 6, "University" zaczyna się od 7,
# spacja = 17, "of" = 18-19, spacja = 20, "Economics" zaczyna się od 21
abbreviation = university[0] + university[7] + university[21]   # K + U + E
print(abbreviation)                                # wypisujemy skrót: KUE
