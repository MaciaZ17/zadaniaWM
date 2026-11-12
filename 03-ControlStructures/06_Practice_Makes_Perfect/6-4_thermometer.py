###
# Program that simulates the operation of an electronic thermometer.
# Testy: 33 -> hot, 30 -> warm, 8 -> cold, 0 -> cold, -2 -> frost
#
temperature = float(input('Enter temperature in Celsius: '))   # wczytujemy temperaturę
if temperature > 35:                                         # powyżej 35 stopni
    print("It is extremely hot")                             # ekstremalnie gorąco
elif temperature > 30:                                       # powyżej 30 (a nie więcej niż 35)
    print("It is hot")                                       # gorąco
elif temperature >= 15:                                      # co najmniej 15
    print("It is warm")                                      # ciepło
elif temperature >= 0:                                       # co najmniej 0
    print("It is cold")                                      # zimno
else:                                                        # poniżej 0
    print("Warning, frost")                                  # ostrzeżenie: mróz
