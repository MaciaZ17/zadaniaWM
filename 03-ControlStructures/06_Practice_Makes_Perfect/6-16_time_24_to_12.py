###
# Konwersja czasu z formatu 24-godzinnego (hh:mm) na 12-godzinny. Przykład: 16:32 -> 4:32pm
#
time_24 = input('Enter time (24-hour format): ')             # wczytujemy czas jako tekst, np. 16:32
hour = int(time_24[0:2])                                     # znaki 0 i 1 to godzina; zamieniamy na liczbę
minutes = time_24[3:5]                                       # znaki 3 i 4 to minuty (zostają tekstem, żeby zachować np. 05)

if hour == 0:                                                # północ
    hour_12 = 12                                             # 00:xx = 12:xx am
    suffix = 'am'                                            # przed południem
elif hour < 12:                                              # godziny 1-11
    hour_12 = hour                                           # bez zmian
    suffix = 'am'                                            # przed południem
elif hour == 12:                                             # południe
    hour_12 = 12                                             # 12:xx pm
    suffix = 'pm'                                            # po południu
else:                                                        # godziny 13-23
    hour_12 = hour - 12                                      # odejmujemy 12
    suffix = 'pm'                                            # po południu

print(f'Time in 12-hour format: {hour_12}:{minutes}{suffix}')   # wypisujemy wynik
