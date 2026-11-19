###
# Returns a string specifying the time in 24-hour
# or 12-hour format and tests the function
#
# f'...' to napis, w którym w nawiasach {} wstawiamy wartości zmiennych.
def time_string(hours, minutes, time_format):          # funkcja zamienia godzinę i minuty na napis z czasem
    result = ''                                        # pusta zmienna na wynik
    if time_format == '24':                            # jeśli chcemy zegar 24-godzinny
        result = f'{hours:02d}:{minutes:02d}'          # :02d dopisuje zero z przodu, gdy liczba ma jedną cyfrę (8 -> 08)
    elif time_format == '12':                          # jeśli chcemy zegar 12-godzinny
        if hours < 12:                                 # godziny od 0 do 11
            suffix = 'am'                              # am znaczy przed południem
        else:                                          # godziny od 12 do 23
            suffix = 'pm'                              # pm znaczy po południu
        if hours == 0:                                 # północ (godzina 0)
            hours_12 = 12                              # w zegarze 12-godzinnym północ to 12
        elif hours > 12:                               # godziny od 13 do 23
            hours_12 = hours - 12                      # odejmujemy 12, np. 19 -> 7
        else:                                          # godziny od 1 do 12
            hours_12 = hours                           # zostają bez zmian
        result = f'{hours_12}:{minutes:02d}{suffix}'   # składamy napis, np. 7:02pm
    return result                                      # funkcja oddaje gotowy napis

def check(result, expected):                           # funkcja do testów: porównuje wynik z tym, co powinno wyjść
    if result == expected:                             # jeśli wynik jest taki, jak powinien
        print('OK   ', result)                         # wypisujemy OK i wynik
    else:                                              # jeśli wynik jest inny
        print('ERROR', result, 'expected', expected)   # wypisujemy błąd i to, co powinno wyjść

# Tests
check(time_string(15, 38, '24'), '15:38')              # powinno wyjść 15:38
check(time_string(8, 3, '24'), '08:03')                # powinno wyjść 08:03
check(time_string(0, 5, '24'), '00:05')                # powinno wyjść 00:05
check(time_string(11, 15, '12'), '11:15am')            # powinno wyjść 11:15am
check(time_string(0, 7, '12'), '12:07am')              # powinno wyjść 12:07am
check(time_string(7, 30, '12'), '7:30am')              # powinno wyjść 7:30am
check(time_string(12, 46, '12'), '12:46pm')            # powinno wyjść 12:46pm
check(time_string(13, 10, '12'), '1:10pm')             # powinno wyjść 1:10pm
check(time_string(19, 2, '12'), '7:02pm')              # w treści jest 02, ale Python nie pozwala na zero przed liczbą, więc 2
