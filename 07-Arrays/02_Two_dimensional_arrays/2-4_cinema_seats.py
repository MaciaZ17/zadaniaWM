###
# Cinema seating: available seats, booked seats and seat status
#
# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]                                                                   # sala: 5 rzędów po 5 miejsc

def seats_total(seats):                                             # funkcja liczy wszystkie miejsca
    count = 0                                                       # licznik, na początku 0
    for row in seats:                                               # bierzemy po kolei każdy rząd
        count = count + len(row)                                    # dodajemy liczbę miejsc w rzędzie
    return count                                                    # funkcja oddaje wynik

def seats_available(seats):                                         # funkcja liczy wolne miejsca
    count = 0                                                       # licznik, na początku 0
    for row in seats:                                               # bierzemy po kolei każdy rząd
        for seat in row:                                            # bierzemy po kolei każde miejsce w rzędzie
            if seat == 'A':                                         # jeśli miejsce jest wolne
                count = count + 1                                   # zwiększamy licznik
    return count                                                    # funkcja oddaje wynik

def seats_booked(seats):                                            # funkcja liczy zajęte miejsca
    count = 0                                                       # licznik, na początku 0
    for row in seats:                                               # bierzemy po kolei każdy rząd
        for seat in row:                                            # bierzemy po kolei każde miejsce
            if seat == 'B':                                         # jeśli miejsce jest zarezerwowane
                count = count + 1                                   # zwiększamy licznik
    return count                                                    # funkcja oddaje wynik

def seat_status(seats, row, place):                                 # funkcja mówi, czy miejsce jest wolne; row i place liczymy od 1
    seat = seats[row - 1][place - 1]                                # odejmujemy 1, bo indeksy liczymy od 0; [rząd][miejsce]
    if seat == 'A':                                                 # jeśli jest A
        return 'available'                                          # miejsce wolne
    else:                                                           # w przeciwnym razie
        return 'booked'                                             # miejsce zajęte

print('CINEMA INFORMATION TABLE')                                   # nagłówek
print('Total seats:', seats_total(cinema_seats))                    # wszystkie miejsca (25)
print('Seats available:', seats_available(cinema_seats))            # wolne miejsca (19)
print('Seats booked:', seats_booked(cinema_seats))                  # zajęte miejsca (6)
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))   # available
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))   # available
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))   # booked
