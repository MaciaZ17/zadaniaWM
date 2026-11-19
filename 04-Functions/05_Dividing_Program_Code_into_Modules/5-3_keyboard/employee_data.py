###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard                                                    # dołączamy nasz plik keyboard.py

# Reads employee's data from keyboard
first_name = keyboard.input_string('Enter name: ')                 # wczytujemy imię; keyboard. przed nazwą, bo funkcja jest w tamtym pliku
last_name = keyboard.input_string('Enter surname: ')               # wczytujemy nazwisko
age = keyboard.input_integer('Enter age: ')                        # wczytujemy wiek jako liczbę całkowitą
salary = keyboard.input_real('Enter salary: ')                     # wczytujemy pensję jako liczbę z groszami
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n) ')   # pytamy, czy ukryć pensję: y daje True, n daje False

# Prints employee's record
print()                                                            # pusta linia, żeby wynik był czytelniejszy
print('DATA RECORD')                                               # nagłówek
print('===========')                                               # linia pod nagłówkiem
print('Name:', first_name)                                         # wypisujemy imię
print('Surname:', last_name)                                       # wypisujemy nazwisko
print('Age:', age)                                                 # wypisujemy wiek
if not is_salary_hidden:                                           # not odwraca True i False, więc warunek działa, gdy pensja nie jest ukryta
    print('Salary:', salary)                                       # wypisujemy pensję
