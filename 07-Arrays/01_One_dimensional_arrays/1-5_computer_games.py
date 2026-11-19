###
# Prints a numbered, alphabetically sorted list of computer games
#
computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]                                          # lista gier

sorted_games = sorted(computer_games)      # sorted() oddaje nową listę ułożoną alfabetycznie

i = 0                                      # i to numer (indeks) gry, zaczynamy od 0
while i < len(sorted_games):               # powtarzamy, dopóki nie przejdziemy wszystkich gier
    print(f'{i + 1}. {sorted_games[i]}')   # wypisujemy numer (i + 1, bo liczymy od 1) i nazwę gry
    i = i + 1                              # przechodzimy do następnej gry
