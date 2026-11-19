###
# Spells out a name entered from the keyboard
# using the ICAO phonetic alphabet
#
def icao_word(letter):                      # tworzymy funkcję, która dla litery zwraca słowo z alfabetu ICAO
    letter = letter.upper()                 # upper() zamienia literę na wielką, więc a i A działają tak samo
    word = ''                               # pusta zmienna, wpiszemy do niej słowo
    if letter == 'A':                       # jeśli litera to A
        word = 'Alfa'                       # słowo to Alfa
    elif letter == 'B':                     # jeśli B
        word = 'Bravo'                      # słowo to Bravo
    elif letter == 'C':                     # jeśli C
        word = 'Charlie'                    # słowo to Charlie
    elif letter == 'D':                     # jeśli D
        word = 'Delta'                      # słowo to Delta
    elif letter == 'E':                     # jeśli E
        word = 'Echo'                       # słowo to Echo
    elif letter == 'F':                     # jeśli F
        word = 'Foxtrot'                    # słowo to Foxtrot
    elif letter == 'G':                     # jeśli G
        word = 'Golf'                       # słowo to Golf
    elif letter == 'H':                     # jeśli H
        word = 'Hotel'                      # słowo to Hotel
    elif letter == 'I':                     # jeśli I
        word = 'India'                      # słowo to India
    elif letter == 'J':                     # jeśli J
        word = 'Juliett'                    # słowo to Juliett
    elif letter == 'K':                     # jeśli K
        word = 'Kilo'                       # słowo to Kilo
    elif letter == 'L':                     # jeśli L
        word = 'Lima'                       # słowo to Lima
    elif letter == 'M':                     # jeśli M
        word = 'Mike'                       # słowo to Mike
    elif letter == 'N':                     # jeśli N
        word = 'November'                   # słowo to November
    elif letter == 'O':                     # jeśli O
        word = 'Oscar'                      # słowo to Oscar
    elif letter == 'P':                     # jeśli P
        word = 'Papa'                       # słowo to Papa
    elif letter == 'Q':                     # jeśli Q
        word = 'Quebec'                     # słowo to Quebec
    elif letter == 'R':                     # jeśli R
        word = 'Romeo'                      # słowo to Romeo
    elif letter == 'S':                     # jeśli S
        word = 'Sierra'                     # słowo to Sierra
    elif letter == 'T':                     # jeśli T
        word = 'Tango'                      # słowo to Tango
    elif letter == 'U':                     # jeśli U
        word = 'Uniform'                    # słowo to Uniform
    elif letter == 'V':                     # jeśli V
        word = 'Victor'                     # słowo to Victor
    elif letter == 'W':                     # jeśli W
        word = 'Whiskey'                    # słowo to Whiskey
    elif letter == 'X':                     # jeśli X
        word = 'X-ray'                      # słowo to X-ray
    elif letter == 'Y':                     # jeśli Y
        word = 'Yankee'                     # słowo to Yankee
    elif letter == 'Z':                     # jeśli Z
        word = 'Zulu'                       # słowo to Zulu
    else:                                   # jeśli to nie litera (np. cyfra albo spacja)
        word = '?'                          # wstawiamy znak zapytania
    return word                             # funkcja oddaje słowo

# Main program - spelling a name
name = input('Enter your name: ')           # wczytujemy imię, np. Wiktor
for letter in name:                         # pętla: bierzemy po kolei każdą literę imienia
    print(letter, '-', icao_word(letter))   # wypisujemy literę i jej słowo, np. W - Whiskey
