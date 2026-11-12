###
# BMI Calculator
# Program uruchamiany w trybie skryptowym: py 1-3_bmi.py
#
height = input('Enter your height in cm: ')   # input() pobiera tekst z klawiatury (zawsze jako string)
weight = input('Enter your weight in kg: ')   # tak samo wczytujemy wagę (jako tekst)
height = int(height)                          # zamieniamy tekst na liczbę całkowitą, żeby można było liczyć
weight = int(weight)                          # to samo dla wagi
bmi = weight / (height/100)**2                # wzór BMI: waga / (wzrost w metrach)^2; /100 zamienia cm na m
bmi = round(bmi,2)                            # zaokrąglamy BMI do 2 miejsc po przecinku
print('Your BMI is', bmi)                     # wypisujemy wynik
print('Check on the Internet if your BMI is ok!!')  # wypisujemy stałą informację
