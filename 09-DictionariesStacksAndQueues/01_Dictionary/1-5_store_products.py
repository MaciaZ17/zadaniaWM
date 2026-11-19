###
# Prints products with quantities and the total number of products
#
products = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}                                            # produkt to klucz, liczba sztuk to wartość

total = 0                                    # suma sztuk, na początku 0
for product, quantity in products.items():   # bierzemy po kolei każdą parę produkt : liczba
    print(product, ':', quantity)            # wypisujemy produkt i liczbę sztuk
    total = total + quantity                 # dodajemy liczbę do sumy

print('Total number of products:', total)    # wypisujemy sumę (330)
