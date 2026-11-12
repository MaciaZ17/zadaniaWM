###
# Calculation of circle area and circumference
# Testy: r=1 -> obwód 6.28, pole 3.14 ; r=3 -> obwód 18.84, pole 28.26
#
# determine radius and PI values
r = float(input('Enter radius: '))                 # wczytujemy promień
pi = 3.14                                          # przyjmujemy pi = 3.14, żeby wyniki zgadzały się z testami
# calculate area
area = pi * r ** 2                                 # pole koła: pi * r^2
# calculate circumference
circumference = 2 * pi * r                         # obwód koła: 2 * pi * r
# print results
print(f'Area: {area:.2f}')                         # wypisujemy pole z 2 miejscami po przecinku
print(f'Circumference: {circumference:.2f}')       # wypisujemy obwód
