###
# Prints a greeting
#
name = ''                                                    # na start imię jest puste, więc pętla na pewno ruszy

while name == '':                                            # powtarzamy pytanie, dopóki użytkownik nic nie wpisze
    name = input('Enter your name: ')                        # wczytujemy imię

print(f'Hello {name}')                                       # po wyjściu z pętli witamy użytkownika
