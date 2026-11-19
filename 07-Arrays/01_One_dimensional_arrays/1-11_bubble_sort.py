###
# Bubble sort
#
# Sortowanie bąbelkowe porównuje sąsiednie elementy i zamienia je, gdy są w złej kolejności.
# Po każdym przejściu największy element "wypływa" na koniec listy.
def bubble_sort(arr):                                             # funkcja sortuje listę od najmniejszej do największej
    n = len(arr)                                                  # n to liczba elementów
    for i in range(n):                                            # robimy n przejść po liście
        for j in range(n - i - 1):                                # porównujemy pary; końcówka listy jest już posortowana, więc jej nie sprawdzamy
            if arr[j] > arr[j + 1]:                               # jeśli element jest większy od następnego
                temp = arr[j]                                     # zamiana miejscami: zapamiętujemy pierwszy element
                arr[j] = arr[j + 1]                               # na jego miejsce wstawiamy drugi
                arr[j + 1] = temp                                 # na miejsce drugiego wstawiamy zapamiętany
    return arr                                                    # funkcja oddaje posortowaną listę

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]        # spalanie samochodów
print(car_fuel_consumption)                                       # wypisujemy przed sortowaniem
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)   # sortujemy
print(sorted_car_fuel_consumption)                                # wypisujemy po sortowaniu

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]         # transakcje bankowe
print(bank_transactions)                                          # wypisujemy przed sortowaniem
sorted_bank_transactions = bubble_sort(bank_transactions)         # sortujemy
print(sorted_bank_transactions)                                   # wypisujemy po sortowaniu
