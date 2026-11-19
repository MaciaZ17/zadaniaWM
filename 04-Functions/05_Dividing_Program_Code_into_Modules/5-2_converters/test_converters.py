###
# Tests the functions from the converters module
#
import converters                                   # dołączamy nasz plik converters.py (nazwę piszemy bez .py)

print('250 cm =', converters.cm_to_m(250), 'm')     # uruchamiamy funkcję z pliku converters i wypisujemy wynik (2.5)
print('1.75 m =', converters.m_to_cm(1.75), 'cm')   # zamieniamy 1.75 m na cm (175.0)

inches = converters.cm_to_inches(100)               # zamieniamy 100 cm na cale
print('100 cm =', round(inches, 2), 'inches')       # round(..., 2) zaokrągla do 2 miejsc po kropce (39.37)

cm = converters.feet_inches_to_cm(5, 11)            # zamieniamy 5 stóp i 11 cali na centymetry
print('5 feet 11 inches =', round(cm, 2), 'cm')     # wypisujemy wynik (180.34)
