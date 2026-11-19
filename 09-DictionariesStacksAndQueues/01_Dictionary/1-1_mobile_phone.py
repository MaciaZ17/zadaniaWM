###
# Describes a mobile phone with a dictionary and prints its contents
#
# Słownik (dictionary) przechowuje pary klucz : wartość. Po kluczu odczytujemy wartość.
mobile = {
    "OS": "Android",
    "brand": "Samsung",
    "model": "Galaxy S24",
    "screen_inches": 6.2,
    "memory_gb": 256,
    "color": "black"
}                                   # słownik z 6 parami klucz : wartość

for key, value in mobile.items():   # items() daje pary (klucz, wartość); bierzemy je po kolei
    print(f"{key} : {value}")       # wypisujemy klucz i wartość, np. OS : Android
