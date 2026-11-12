###
# A program that reads temperature in degrees Celsius from the keyboard.
# Algorytm: 1) wczytaj °C, 2) przelicz na Kelviny, 3) przelicz na Fahrenheity, 4) wypisz.
#

# 1) wczytujemy temperaturę w stopniach Celsjusza
celsius = float(input('Enter temperature in Celsius: '))   # float, bo temperatura może mieć część dziesiętną
# 2) Kelvin = Celsius + 273.15
kelvin = celsius + 273.15                          # skala Kelvina jest przesunięta o 273.15
# 3) Fahrenheit = Celsius * 9/5 + 32
fahrenheit = celsius * 9 / 5 + 32                  # wzór na przeliczenie °C -> °F
# 4) wypisujemy wyniki
print(f'{celsius} C = {kelvin:.2f} K')             # wynik w Kelvinach
print(f'{celsius} C = {fahrenheit:.2f} F')         # wynik w Fahrenheitach
