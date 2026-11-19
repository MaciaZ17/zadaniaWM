###
# Prints vehicle registration numbers from Krakow
#
polish_license_plates = [
    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
    'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
    'KK54985', 'LU4864U'
]                                                            # lista numerów rejestracyjnych

counter = 1                                                  # numer na wypisanej liście, zaczynamy od 1
for car_number in polish_license_plates:                     # pętla: bierzemy po kolei każdy numer
    if car_number[0:2] == 'KR' or car_number[0:2] == 'KK':   # [0:2] bierze 2 pierwsze litery; sprawdzamy, czy to KR lub KK
        print(counter, car_number)                           # wypisujemy numer na liście i rejestrację
        counter += 1                                         # += 1 to skrót od counter = counter + 1
