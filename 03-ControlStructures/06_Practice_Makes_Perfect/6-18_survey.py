###
# Ankieta z trzema pytaniami tak/nie; odpowiedzi zapisujemy w zmiennych logicznych.
#
print('SURVEY')                                              # nagłówek ankiety
interested = input('Are you interested in computer science? (y/n): ') == 'y'   # True, gdy odpowiedź to y
games = input('Do you like playing computer games? (y/n): ') == 'y'            # j.w.
instagram = input('Do you have an Instagram account? (y/n): ') == 'y'         # j.w.

if interested:                                               # zamiana True/False na Yes/No
    interested_text = 'Yes'                                  # tak
else:                                                        # nie
    interested_text = 'No'                                   # nie
if games:                                                    # drugie pytanie
    games_text = 'Yes'                                       # tak
else:                                                        # nie
    games_text = 'No'                                        # nie
if instagram:                                                # trzecie pytanie
    instagram_text = 'Yes'                                   # tak
else:                                                        # nie
    instagram_text = 'No'                                    # nie

print('SURVEY RESULTS')                                      # nagłówek wyników
print(f'Interested in computer science: {interested_text}')  # wynik 1
print(f'Playing computer games: {games_text}')               # wynik 2
print(f'Has an Instagram account: {instagram_text}')        # wynik 3
