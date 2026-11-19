###
# Displays hotels and average room prices in Krakow and Sopot
# and indicates in which city hotels are cheaper
#
hotels_in_Krakow = [
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00}
]                                                              # hotele w Krakowie: każdy to słownik z nazwą i ceną

hotels_in_Sopot = [
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00}
]                                                              # hotele w Sopocie

def hotel_list(hotels):                                        # funkcja zwraca nazwy hoteli oddzielone przecinkami
    names = ''                                                 # pusty napis na start
    for i in range(len(hotels)):                               # i to kolejne indeksy hoteli
        if i > 0:                                              # jeśli to nie pierwszy hotel
            names = names + ','                                # doklejamy przecinek
        names = names + hotels[i]['name']                      # doklejamy nazwę hotelu
    return names                                               # funkcja oddaje napis z nazwami

def avg_price(hotels):                                         # funkcja zwraca średnią cenę pokoju, zaokrągloną do całości
    total = 0                                                  # suma cen, na początku 0
    for hotel in hotels:                                       # bierzemy po kolei każdy hotel
        total = total + hotel['price']                         # dodajemy jego cenę
    return round(total / len(hotels))                          # średnia = suma / liczba hoteli; round() bez drugiej liczby zaokrągla do całości

def main():                                                    # program główny
    krakow_avg = avg_price(hotels_in_Krakow)                   # średnia w Krakowie
    sopot_avg = avg_price(hotels_in_Sopot)                     # średnia w Sopocie
    print('Hotels in Krakow:', hotel_list(hotels_in_Krakow))   # wypisujemy hotele w Krakowie
    print('Average hotel price in Krakow:', krakow_avg)        # średnia 402.5; round() zaokrągla .5 do liczby parzystej, więc 402
    print('Hotels in Sopot:', hotel_list(hotels_in_Sopot))     # hotele w Sopocie
    print('Average hotel price in Sopot:', sopot_avg)          # i średnią cenę (414)
    if krakow_avg < sopot_avg:                                 # jeśli w Krakowie jest taniej
        print('Cheaper hotels in: Krakow')                     # wypisujemy wynik
    elif sopot_avg < krakow_avg:                               # jeśli w Sopocie jest taniej
        print('Cheaper hotels in: Sopot')                      # wypisujemy wynik
    else:                                                      # jeśli ceny są równe
        print('Hotels cost the same in both cities')           # wypisujemy wynik

if __name__ == "__main__":                                     # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                     # wtedy uruchamiamy program główny
