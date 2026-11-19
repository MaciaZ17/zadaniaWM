###
# Creates a shopping list based on product names
# entered from the keyboard.
#

# shopping list file name
shopping_list = 'shopping_list.txt'                     # nazwa pliku z listą zakupów

# adds product name at the end of a shopping list
def add_product(file_name, product_name):               # funkcja dopisuje produkt na koniec pliku
    with open(file_name, 'a') as file:                  # 'a' (append) dopisuje na końcu, nie kasuje tego, co już jest
        file.write(product_name + '\n')                 # zapisujemy produkt i przechodzimy do nowej linii

# Takes next product name from the keyboard
product = ""                                            # pusta zmienna na start, żeby pętla mogła ruszyć
while product != "0":                                   # powtarzamy, dopóki ktoś nie wpisze 0
    product = input('Enter product name (0 stops): ')   # wczytujemy nazwę produktu
    if product == '0':                                  # jeśli wpisano 0
        break                                           # break od razu kończy pętlę while
    else:                                               # w przeciwnym razie
        add_product(shopping_list, product)             # dopisujemy produkt do pliku

print('Shopping list saved to', shopping_list)          # informujemy, gdzie jest lista
