###
# Returns True if at least 3 people were in the room
# at the same time ('+' = person entering, '-' = person leaving)
#
def f(detector):                                            # funkcja sprawdza, czy w pokoju były naraz co najmniej 3 osoby
    people = 0                                              # ile osób jest teraz w pokoju; na początku 0
    for sign in detector:                                   # pętla: bierzemy po kolei każdy znak z czujnika
        if sign == '+':                                     # jeśli ktoś wszedł
            people = people + 1                             # dodajemy 1 osobę
        elif sign == '-':                                   # jeśli ktoś wyszedł
            people = people - 1                             # odejmujemy 1 osobę
        if people >= 3:                                     # jeśli w pokoju są 3 osoby lub więcej
            return True                                     # oddajemy True i kończymy
    return False                                            # nigdy nie było 3 osób naraz, więc False

def main():                                                 # program główny
    print('f("+-+++-+---") returns', f("+-+++-+---"))       # powinno wyjść True
    print('f("+-+-+-+-") returns', f("+-+-+-+-"))           # powinno wyjść False
    print('f("+-++-+--") returns', f("+-++-+--"))           # powinno wyjść False
    print('f("+-++-++-+---") returns', f("+-++-++-+---"))   # powinno wyjść True

if __name__ == "__main__":                                  # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                  # wtedy uruchamiamy program główny
