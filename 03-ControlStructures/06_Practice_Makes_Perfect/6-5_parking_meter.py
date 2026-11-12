###
# Parking meter: 1-2 h: 5 PLN, 3-6 h: 15 PLN, over 6 h: 20 PLN
#
hours = int(input('Enter number of parking hours: '))        # wczytujemy liczbę godzin
if hours < 1:                                                # mniej niż 1 godzina nie ma sensu
    print('Incorrect number of hours')                       # komunikat o błędzie
elif hours <= 2:                                             # 1-2 godziny
    print('Parking fee: 5 PLN')                              # opłata 5 zł
elif hours <= 6:                                             # 3-6 godzin
    print('Parking fee: 15 PLN')                             # opłata 15 zł
else:                                                        # powyżej 6 godzin
    print('Parking fee: 20 PLN')                             # opłata 20 zł
