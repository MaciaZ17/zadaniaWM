###
# Czy tablica rejestracyjna jest z Krakowa (zaczyna się od KR lub KK)?
# W oryginale brakowało litery f przed apostrofem w ostatnim print - bez niej
# Python wypisałby dosłownie {is_krakow} zamiast True/False.
#
car_number = input('Enter car registration number: ')   # wczytujemy numer rejestracyjny
is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"   # pierwsze 2 znaki to KR albo KK
print(f'Car is from Krakow: {is_krakow}')          # f-string, żeby wstawić wartość zmiennej
