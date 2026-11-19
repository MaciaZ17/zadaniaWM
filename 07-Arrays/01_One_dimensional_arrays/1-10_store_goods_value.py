###
# Calculates the value of all the goods available in the store
#
# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]  # ceny produktów

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]             # liczba sztuk; ten sam indeks = ten sam produkt

total_value = 0                                                       # wartość wszystkich towarów, na początku 0
for i in range(len(product_prices)):                                  # i to kolejne indeksy produktów: 0, 1, ... 9
    total_value = total_value + product_prices[i] * product_quantities[i]  # cena razy liczba sztuk, dodajemy do sumy

print('The value of all goods in the store:', round(total_value, 2))  # wypisujemy wynik zaokrąglony do groszy
