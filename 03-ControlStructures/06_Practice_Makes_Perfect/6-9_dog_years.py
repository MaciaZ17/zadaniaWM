###
# Dog's age: pierwsze 2 lata = 10.5 roku człowieka każdy, potem 4 lata za każdy rok.
# Przykład: 15 -> 2*10.5 + 13*4 = 73
#
human_age = int(input("Enter the dog's age in human years: "))   # wiek psa w latach
if human_age <= 2:                                           # dla psa do 2 lat
    dog_age = human_age * 10.5                               # każdy rok to 10.5
else:                                                        # dla starszego psa
    dog_age = 21 + (human_age - 2) * 4                       # 21 za pierwsze dwa lata + 4 za każdy kolejny rok
print(f"The dog's age in dog's years is {dog_age} years.")   # wypisujemy wynik
