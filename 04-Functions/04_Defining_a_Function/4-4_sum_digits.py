###
# Calculates the sum of the digits in a number
#
def sum_digits(number):                                               # tworzymy funkcję, która sumuje cyfry liczby
    number = abs(number)                                              # usuwamy minus, jeśli liczba jest ujemna
    digits = str(number)                                              # zamieniamy liczbę na napis, żeby brać cyfry po kolei
    total = 0                                                         # tu będziemy dodawać cyfry; zaczynamy od 0
    for digit in digits:                                              # pętla: bierzemy po kolei każdą cyfrę
        total = total + int(digit)                                    # zamieniamy cyfrę na liczbę i dodajemy do sumy
    return total                                                      # funkcja oddaje sumę cyfr

any_number = int(input('Enter integer number: '))                     # wczytujemy liczbę z klawiatury
result = sum_digits(any_number)                                       # uruchamiamy funkcję, wynik zapisujemy w result
print('The sum of the digits in the number', any_number, 'is', result)  # wypisujemy wynik, np. dla 385: 3+8+5 = 16
