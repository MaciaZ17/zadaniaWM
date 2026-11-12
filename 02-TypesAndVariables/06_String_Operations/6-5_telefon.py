###
# Numer telefonu w grupach po 3 cyfry oddzielonych myślnikiem.
#
phone = input('Enter phone number: ')              # wczytujemy 9 cyfr jako tekst (nie zamieniamy na int!)
formatted = phone[0:3] + '-' + phone[3:6] + '-' + phone[6:9]   # trzy kawałki po 3 znaki połączone myślnikami
print(f'Phone number: {formatted}')                # np. 543-097-329
