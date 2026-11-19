###
# Creates the person dictionary from two other dictionaries
#
basic_data = {
    "name": "Barbara",
    "age": 21
}                                          # pierwszy słownik

advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}                                          # drugi słownik

person = {}                                # pusty słownik na wszystkie dane
for key, value in basic_data.items():      # bierzemy po kolei pary z pierwszego słownika
    person[key] = value                    # i dodajemy je do person
for key, value in advanced_data.items():   # to samo dla drugiego słownika
    person[key] = value                    # dodajemy pary do person

print(person)                              # wypisujemy słownik z pięcioma parami
