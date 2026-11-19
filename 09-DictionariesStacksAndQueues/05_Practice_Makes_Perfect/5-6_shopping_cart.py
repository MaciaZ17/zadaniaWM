###
# Calculates the total cost of a shopping cart using a price list
#
# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}  # produkt to klucz, cena to wartość

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}                            # produkt to klucz, liczba sztuk to wartość

# Calculate total cost
total = 0                                                             # suma, na początku 0
for product, quantity in cart.items():                                # bierzemy po kolei każdy produkt z koszyka i jego liczbę
    total = total + prices[product] * quantity                        # cenę z cennika mnożymy przez liczbę sztuk i dodajemy do sumy

print('Total cost:', round(total, 2))                                 # wypisujemy sumę zaokrągloną do groszy (8.54)
