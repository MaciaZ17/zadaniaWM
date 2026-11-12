###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. The program calculates
# total fuel consumption for a given distance in km and a given driving mode.
# Testy: 200 km M -> 18 l ; 400 km A -> 28 l ; 350 km E -> 21 l
#
driving_mode = input('Enter driving mode (A/M/E): ')         # wczytujemy tryb jazdy jako tekst
distance = int(input('Enter distance in km: '))              # wczytujemy dystans w km jako liczbę całkowitą
fuel_consumption = 0                                         # spalanie na 100 km (na razie 0)
mode_ok = True                                               # flaga: czy tryb jest poprawny (zakładamy, że tak)

if driving_mode == 'A':                                      # tryb Auto
    fuel_consumption = 7                                     # 7 litrów na 100 km
elif driving_mode == 'M':                                    # tryb Manual
    fuel_consumption = 9                                     # 9 litrów na 100 km
elif driving_mode == 'E':                                    # tryb Eco
    fuel_consumption = 6                                     # 6 litrów na 100 km
else:                                                        # nieznany tryb
    mode_ok = False                                          # zaznaczamy, że tryb jest błędny

if mode_ok:                                                  # liczymy tylko dla poprawnego trybu
    total_consumption = distance * fuel_consumption / 100    # spalanie całkowite = dystans * (litry na 100 km) / 100
    print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')   # wynik
else:                                                        # dla błędnego trybu
    print('Incorrect driving mode')                          # komunikat o błędzie
