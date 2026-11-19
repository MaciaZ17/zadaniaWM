###
# Checks the correctness of username and password
#
import re                                                             # moduł do wyrażeń regularnych

# read username and password from keyboard
username = input('Enter username: ')                                  # wczytujemy nazwę użytkownika
password = input('Enter password: ')                                  # wczytujemy hasło

# pattern (criteria) for username and password
# ^ to początek napisu, $ to koniec, więc cały napis musi pasować do wzorca.
username_pattern = r'^[a-z]{6,}$'                                     # tylko małe litery, co najmniej 6 znaków ({6,} = 6 lub więcej)
password_pattern = r'^[A-Za-z0-9_]{8,}$'                              # litery małe i wielkie, cyfry i _, co najmniej 8 znaków

# check if username and password are ok
username_match = re.match(username_pattern, username)                 # re.match oddaje wynik, gdy pasuje, albo None, gdy nie pasuje
password_match = re.match(password_pattern, password)                 # to samo dla hasła

# print results
# W if None działa jak False, a znaleziony wynik jak True.
if username_match and password_match:                                 # jeśli oba pasują
    print('Username and password are correct.')                       # wszystko dobrze
else:                                                                 # jeśli któryś nie pasuje
    if not username_match:                                            # jeśli nazwa nie pasuje
        print('Username must have at least 6 characters, only lowercase letters.')  # mówimy, co poprawić
    if not password_match:                                            # jeśli hasło nie pasuje
        print('Password must have at least 8 characters: letters, digits or _ only.')  # mówimy, co poprawić
