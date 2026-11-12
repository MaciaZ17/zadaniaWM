###
# timer.py - odliczanie do zera (wersja z modyfikacją: ostatnie 5 sekund słownie)
# UWAGA: nie miałem Twojego oryginalnego timer.py, więc napisałem własną wersję;
# jeśli Twój wygląda inaczej, wystarczy przenieść blok if/elif do swojej pętli.
#
# import time                                                # (opcjonalnie) odkomentuj, żeby odliczanie trwało naprawdę po 1 sekundzie
number = int(input('Enter number of seconds: '))             # wczytujemy liczbę sekund

while number > 0:                                            # odliczamy, dopóki zostały jeszcze sekundy
    if number == 5:                                          # pięć sekund do końca
        print('five')                                        # wypisujemy słownie
    elif number == 4:                                        # cztery
        print('four')                                        # słownie
    elif number == 3:                                        # trzy
        print('three')                                       # słownie
    elif number == 2:                                        # dwie
        print('two')                                         # słownie
    elif number == 1:                                        # jedna
        print('one')                                         # słownie
    else:                                                    # więcej niż 5 sekund
        print(number)                                        # wypisujemy zwykłą liczbą
    # time.sleep(1)                                          # (opcjonalnie) odkomentuj, żeby zatrzymać program na 1 sekundę
    number -= 1                                              # zmniejszamy licznik o 1

print('0 - Time is up!')                                     # po zakończeniu pętli informujemy o końcu
