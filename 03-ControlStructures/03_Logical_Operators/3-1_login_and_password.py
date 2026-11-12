###
# Checking login and password
#
login = 'joe'                                                # poprawny login
password = 'abcd'                                            # poprawne hasło
entered_login = input('Login: ')                             # login wpisany przez użytkownika
entered_password = input('Password: ')                       # hasło wpisane przez użytkownika
if login == entered_login and password == entered_password:  # and: oba warunki muszą być prawdziwe jednocześnie
    print('You are logged in')                               # logowanie udane
else:                                                        # w oryginale brakowało dwukropka po else
    print('Incorrect login or password!!')                   # logowanie nieudane
