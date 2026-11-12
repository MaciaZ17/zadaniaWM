###
# A program that prints your height both in cm and in feet and inches.
# 1 cal (inch) = 2.54 cm, 1 stopa (foot) = 12 cali
#
cm = 170                                           # wzrost w cm (wpisz swój)
total_inches = round(cm / 2.54)                    # zamieniamy cm na cale i zaokrąglamy do całości (170 cm -> 67 cali)
feet = total_inches // 12                          # dzielenie bez reszty: ile pełnych stóp (67 // 12 = 5)
inches = total_inches % 12                         # reszta z dzielenia: ile cali zostało (67 % 12 = 7)
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')   # wypisujemy wynik
