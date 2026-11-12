# A program that reads your first and last name from the keyboard.
# Store this data in two separate variables.
# Then, print your full name i.e. first and last name separated by a single space.
first_name = input('Enter your first name: ')      # wczytujemy imię jako tekst
last_name = input('Enter your last name: ')        # wczytujemy nazwisko jako tekst
full_name = first_name + ' ' + last_name           # łączymy teksty (+), w środku wstawiamy spację
print(f'Your first name is {first_name} and your last name is {last_name}')   # wypisujemy imię i nazwisko osobno
print(f'And your full name is {full_name}')        # wypisujemy pełne imię i nazwisko
