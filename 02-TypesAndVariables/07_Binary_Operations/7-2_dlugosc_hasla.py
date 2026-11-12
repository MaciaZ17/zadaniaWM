###
# Poprawne hasło ma co najmniej 8 znaków.
# Testy: university (True), peter123 (True), seven (False), anna333 (False)
#
password = input('Enter password: ')               # wczytujemy hasło jako tekst
password_ok = len(password) >= 8                   # len() liczy znaki, >= 8 sprawdza warunek "co najmniej 8"
print(f'Password length is valid: {password_ok}')  # wypisujemy True lub False
