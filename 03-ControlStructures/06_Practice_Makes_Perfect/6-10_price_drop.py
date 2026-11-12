###
# Rekomendacja zakupu, gdy cena spadła o co najmniej 10%.
#
current_price = 140.00                                       # obecna cena
previous_price = 200.00                                      # poprzednia cena
reduction = (previous_price - current_price) / previous_price * 100   # obniżka w procentach: (spadek / stara cena) * 100
print(f'Current product price: {current_price:.2f}')         # wypisujemy obecną cenę
print(f'Previous product price: {previous_price:.2f}')       # wypisujemy poprzednią cenę
if reduction >= 10:                                          # obniżka co najmniej 10%
    print('Buy the product!!')                               # rekomendacja
    print(f'Product price reduced by {reduction:.0f}%')      # :.0f - bez miejsc po przecinku
