###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140                                            # limit prędkości na autostradzie w Polsce
car_speed = int( input('Enter car speed (km/h): ') )         # wczytujemy prędkość i zamieniamy tekst na liczbę całkowitą

if car_speed > speed_limit:                                  # warunek: prędkość większa niż limit (przekroczenie)
    print(f'Your speed is {car_speed}km/h')                  # wypisujemy prędkość kierowcy (blok wcięty = wykona się tylko gdy warunek prawdziwy)
    print('Warning: speed limit exceeded!!')                 # wypisujemy ostrzeżenie
