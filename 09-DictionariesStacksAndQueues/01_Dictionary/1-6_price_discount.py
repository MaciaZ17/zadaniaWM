###
# Prints prices before and after a 10% discount
# and the total value of products
#
price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}                                                               # produkt to klucz, cena to wartość

print('BEFORE DISCOUNT')                                        # nagłówek
total = 0                                                       # suma cen, na początku 0
for product, price in price_list.items():                       # bierzemy po kolei każdą parę produkt : cena
    print(product, ':', price)                                  # wypisujemy produkt i cenę
    total = total + price                                       # dodajemy cenę do sumy
print('Total:', round(total, 2))                                # suma przed obniżką (235.95)

for product in price_list:                                      # pętla po słowniku daje same klucze (nazwy produktów)
    price_list[product] = round(price_list[product] * 0.9, 2)   # cena razy 0.9 to cena po obniżce o 10%; zaokrąglamy do groszy

print()                                                         # pusta linia
print('AFTER 10% DISCOUNT')                                     # nagłówek
total = 0                                                       # liczymy sumę od nowa
for product, price in price_list.items():                       # bierzemy po kolei każdą parę
    print(product, ':', price)                                  # wypisujemy nową cenę
    total = total + price                                       # dodajemy ją do sumy
print('Total:', round(total, 2))                                # suma po obniżce
