###
# Module with a function that masks a credit card number
#
def hide(card_number):                     # funkcja ukrywa środek numeru karty
    first_two = card_number[:2]            # [:2] bierze 2 pierwsze znaki: 52
    last_four = card_number[-4:]           # [-4:] bierze 4 ostatnie znaki: 9022
    stars = '*' * (len(card_number) - 6)   # robimy tyle gwiazdek, ile cyfr ukrywamy (16 - 6 = 10)
    return first_two + stars + last_four   # sklejamy trzy części w jeden napis i go oddajemy
