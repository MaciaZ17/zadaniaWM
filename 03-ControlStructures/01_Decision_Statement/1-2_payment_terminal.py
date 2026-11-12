###
# Credit card payment
# Testy: 140 -> OK, 499 -> OK, 500 -> OK, 501 -> brak środków, 720 -> brak środków
#
account_balance = 500                                        # stan konta klienta
total_payment = float(input('Enter total payment: '))        # wczytujemy kwotę zakupów (float, bo kwota może mieć grosze)

if total_payment <= account_balance:                         # płatność możliwa, gdy kwota nie przekracza stanu konta (500 też przechodzi)
    print('Payment completed')                               # komunikat o udanej płatności
else:                                                        # w przeciwnym razie (kwota > stan konta)
    print('No funds')                                        # komunikat o braku środków
