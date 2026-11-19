###
# The weather station report
#
temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]                                                                   # temperatury z każdego dnia marca

# number of measurements
measurements = len(temperatures)                                    # liczba pomiarów to liczba elementów listy

# calculates average temperature
temp_total = 0                                                      # suma temperatur, na początku 0
for temp in temperatures:                                           # pętla: bierzemy po kolei każdą temperaturę
    temp_total = temp_total + temp                                  # dodajemy ją do sumy
avg_temp = temp_total / measurements                                # średnia = suma / liczba pomiarów

# calculates min and max temperatures
min_temp = min(temperatures)                                        # min() wybiera najniższą temperaturę
max_temp = max(temperatures)                                        # max() wybiera najwyższą temperaturę

# calculates number of days with negative temp
negative_temp = 0                                                   # licznik dni z temperaturą poniżej zera
i = 0                                                               # i to numer dnia na liście, zaczynamy od 0
while i < measurements:                                             # powtarzamy dla każdego dnia
    if temperatures[i] < 0:                                         # jeśli temperatura jest ujemna
        negative_temp = negative_temp + 1                           # zwiększamy licznik o 1
    i = i + 1                                                       # przechodzimy do następnego dnia

# prints out month report
print('TEMPERATURE REPORT')                                         # nagłówek raportu
print('Month: March')                                               # miesiąc
print('Number of measurements:', measurements)                      # liczba pomiarów
print('Average temperature in the month:', round(avg_temp, 2))      # średnia zaokrąglona do 2 miejsc
print('Minimum temperature:', min_temp)                             # najniższa temperatura
print('Maximum temperature:', max_temp)                             # najwyższa temperatura
print('Number of days with negative temperature:', negative_temp)   # liczba dni z ujemną temperaturą
