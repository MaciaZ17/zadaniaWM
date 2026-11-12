###
# Age groups: Child <13, Teen 13-19, Adult 20-64, Senior 65+
#
age = int(input('Enter your age: '))                         # wczytujemy wiek
if age < 13:                                                 # poniżej 13 lat
    print('Child')                                           # dziecko
elif age <= 19:                                              # 13-19 lat
    print('Teen')                                            # nastolatek
elif age <= 64:                                              # 20-64 lata
    print('Adult')                                           # dorosły
else:                                                        # 65 i więcej
    print('Senior')                                          # senior
