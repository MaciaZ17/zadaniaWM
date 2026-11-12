###
# 25% rabatu za każdy produkt ponad dwa. Przykład: 5 szt. po 40 -> 170.00
#
count = int(input('Number of products purchased: '))         # liczba kupionych produktów
price = float(input('Product price: '))                     # cena jednego produktu
if count <= 2:                                               # do dwóch sztuk bez rabatu
    amount = count * price                                   # pełna cena
else:                                                        # powyżej dwóch sztuk
    amount = 2 * price + (count - 2) * price * 0.75          # dwie sztuki po pełnej cenie + reszta z rabatem 25% (cena * 0.75)
print(f'Amount to pay: {amount:.2f}')                        # wypisujemy kwotę z 2 miejscami
