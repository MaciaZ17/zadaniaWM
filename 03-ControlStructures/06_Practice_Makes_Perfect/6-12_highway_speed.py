###
# Speed on highways: at least 40 and at most 140 km/h
#
speed_limit_min = 40                                         # minimalna dozwolona prędkość
speed_limit_max = 140                                        # maksymalna dozwolona prędkość
car_speed = int(input('Enter car speed: '))                  # wczytujemy prędkość samochodu
if car_speed < speed_limit_min or car_speed > speed_limit_max:   # za wolno LUB za szybko
    print('Warning: invalid car speed!!')                    # ostrzeżenie
