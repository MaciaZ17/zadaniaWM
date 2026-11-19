###
# Reads product data from the keyboard and saves it to product.json
#
import json                                                 # moduł do plików JSON

product = {}                                                # pusty słownik na dane produktu

# read product data from keyboard
product['name'] = input('Product name: ')                   # nazwa to napis (str)
product['price'] = round(float(input('Price: ')), 2)        # cena to liczba z kropką (float), zaokrąglona do 2 miejsc
answer = input('Paid (yes/no): ')                           # wczytujemy odpowiedź
product['paid'] = (answer == 'yes')                         # porównanie daje True albo False (bool)

# save product data to json file
with open('product.json', 'w', encoding='utf-8') as file:   # otwieramy plik do zapisu
    json.dump(product, file, indent=4)                      # zapisujemy słownik jako JSON

print('Saved:', product)                                    # wypisujemy, co zapisaliśmy
