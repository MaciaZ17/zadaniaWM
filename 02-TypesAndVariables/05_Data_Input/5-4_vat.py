###
# Program wczytuje kwotę i liczy z niej 23% VAT (zgodnie z przykładem z zadania:
# 15.84 -> 3.64, czyli 15.84 * 0.23).
#
amount = float(input('Enter amount: '))            # wczytujemy kwotę jako liczbę zmiennoprzecinkową
vat = amount * 0.23                                # 23% = 0.23, mnożymy kwotę przez 0.23
print(f'Amount  : {amount:5.2f}')                  # :5.2f = szerokość min. 5 znaków, 2 miejsca po przecinku
print(f'VAT 23% : {vat:5.2f}')                     # tak samo formatujemy VAT, dzięki temu liczby są równo pod sobą
