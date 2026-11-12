###
# House lighting with three bulbs and two switches
# Przełącznik 1 zapala 1 żarówkę, przełącznik 2 zapala 2 żarówki.
#
light_switch1 = True                                         # True - włączony, False - wyłączony (zmieniaj, żeby testować)
light_switch2 = True                                         # drugi przełącznik
bulbs_on = 0                                                 # liczba świecących żarówek
if light_switch1:                                            # jeśli pierwszy przełącznik włączony
    bulbs_on += 1                                            # świeci 1 żarówka
if light_switch2:                                            # jeśli drugi przełącznik włączony
    bulbs_on += 2                                            # świecą 2 żarówki
print(f'Number of bulbs on: {bulbs_on}')                     # wypisujemy wynik (0, 1, 2 albo 3)
