###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))                    # dystans w km (liczba całkowita)
fuel_price = float(input('Enter fuel price per liter: '))          # cena 1 litra paliwa
fuel_consumption = float(input('Enter fuel consumption per 100 km: '))  # spalanie w litrach na 100 km
total_fuel_consumption = distance * fuel_consumption / 100        # ile litrów zużyjemy na całej trasie
total_cost = total_fuel_consumption * fuel_price                  # koszt = litry * cena litra
print(f'Total fuel consumption: {total_fuel_consumption:.2f} l')  # wypisujemy zużycie paliwa
print(f'Total cost: {total_cost:.2f}')                            # wypisujemy koszt
