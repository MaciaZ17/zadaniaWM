###
# Cena po rabacie. Przykład: 24.72 i 15% -> 21.01, obniżka 3.71
#
price = float(input('Enter price: '))              # wczytujemy cenę (float, bo ma grosze)
discount = float(input('Enter discount %: '))      # wczytujemy rabat w procentach
reduction = price * discount / 100                 # kwota obniżki: cena * procent / 100
price_with_discount = price - reduction            # cena po rabacie = cena - obniżka
print(f'Price with discount: {price_with_discount:.2f}')   # wypisujemy cenę po rabacie (2 miejsca)
print(f'Reduction: {reduction:.2f}')                       # wypisujemy różnicę cen (2 miejsca)
