###
# Reads, modifies and prints the person dictionary
#
# Typy wartości: name i surname to napisy (str), age to liczba całkowita (int),
# hobby to lista (list), married to wartość logiczna (bool), phone to słownik (dict).
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}                                           # słownik z danymi osoby

print('Name:', person['name'])              # odczytujemy wartość po kluczu 'name'
print('Hobby:', person['hobby'])            # odczytujemy listę hobby
print(person)                               # wypisujemy cały słownik

person['surname'] = 'Nowak'                 # zmieniamy nazwisko: przypisujemy nową wartość do istniejącego klucza
person['married'] = not person['married']   # not odwraca True na False (i odwrotnie), więc stan cywilny się zmienia
person['gender'] = 'male'                   # nowy klucz: przypisanie do klucza, którego nie było, dodaje go do słownika
person['hobby'].append('bicycle')           # hobby to lista, więc append() dopisuje do niej nowe hobby
person['phone']['work'] = '313131444'       # phone to słownik w słowniku; dodajemy do niego klucz 'work'

for key, value in person.items():           # bierzemy po kolei każdą parę klucz : wartość
    print(key, ':', value)                  # wypisujemy ją
