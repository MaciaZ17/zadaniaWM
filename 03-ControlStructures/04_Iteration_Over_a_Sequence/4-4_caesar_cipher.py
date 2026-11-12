###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position (a -> b, b -> c, ...)
#
plain_text = 'The early bird catches the worm'                # tekst jawny
encrypted_text = ''                                          # pusty tekst na zaszyfrowany wynik

for char in plain_text:                                      # idziemy po kolei po każdym znaku
    if char == ' ':                                          # spacji nie szyfrujemy (inaczej zamieniłaby się w '!')
        encrypted_text = encrypted_text + char               # dopisujemy spację bez zmian
    else:                                                    # dla liter
        # read the character's code (use ord())
        code = ord(char)                                     # pobieramy kod litery
        # add one to the character's code
        if char == 'z':                                      # litera z jest ostatnia w alfabecie
            new_code = ord('a')                              # po z wracamy do a
        elif char == 'Z':                                    # wielkie Z też zawijamy
            new_code = ord('A')                              # po Z wracamy do A
        else:                                                # każda inna litera
            new_code = code + 1                              # zwiększamy kod o 1 (przesunięcie o jedną literę)
        # replace new character code with its corresponding character (use chr())
        new_char = chr(new_code)                             # zamieniamy nowy kod z powrotem na znak
        # add encrypted character to encrypted text
        encrypted_text = encrypted_text + new_char           # dopisujemy zaszyfrowany znak do wyniku

print(plain_text)                                            # tekst jawny
print(encrypted_text)                                        # tekst zaszyfrowany: Uif fbsmz cjse dbudifs uif xpsn
