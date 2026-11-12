###
# Password validator
# New password is at least 12 characters long
#
new_password = input('Enter new password: ')                 # wczytujemy hasło
if len(new_password) < 12:                                   # len() liczy znaki; mniej niż 12 = za krótkie
    print('Password too short (min. 12 chars)')              # komunikat o błędzie
else:                                                        # co najmniej 12 znaków
    print('Password accepted')                               # hasło jest OK
