###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
# Testy: 72 tak, 65 tak, 64 nie, 18 nie, 17 tak
#
age = int(input('Enter your age: '))                         # wczytujemy wiek

if age < 18 or age >= 65:                                    # or: wystarczy, że jeden z warunków jest prawdziwy
    print('You are eligible for a discount')                 # zniżka przysługuje
else:                                                        # w przeciwnym razie
    print('No discount available')                           # zniżka nie przysługuje
