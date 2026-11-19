###
# Simulates the Back key in a web browser
#
import queue                                          # moduł z gotowym stosem

history = queue.LifoQueue()                           # stos odwiedzonych stron
current_page = ''                                     # strona, na której teraz jesteśmy (na początku żadna)

while True:                                           # pętla działa, dopóki nie wybierzemy 0
    print()                                           # pusta linia dla czytelności
    print('Current page:', current_page)              # pokazujemy obecną stronę
    print('1. Go to a new website')                   # opcje menu
    print('2. Back')                                  # kolejna opcja menu
    print('0. Quit')                                  # kolejna opcja menu
    option = input('Select an option: ')              # wczytujemy wybór

    if option == '1':                                 # nowa strona
        new_page = input('Enter website address: ')   # wczytujemy adres
        if current_page != '':                        # jeśli jesteśmy już na jakiejś stronie
            history.put(current_page)                 # odkładamy ją na stos, żeby móc do niej wrócić
        current_page = new_page                       # przechodzimy na nową stronę
    elif option == '2':                               # przycisk Wstecz
        if history.empty():                           # jeśli stos jest pusty
            print('There is no previous page.')       # nie ma do czego wracać
        else:                                         # w przeciwnym razie
            current_page = history.get()              # zdejmujemy ostatnio odwiedzoną stronę i na nią wracamy
            print('Back to:', current_page)           # informujemy, gdzie wróciliśmy
    elif option == '0':                               # wyjście
        break                                         # kończymy pętlę
    else:                                             # inna odpowiedź
        print('Unknown option.')                      # informujemy o złym wyborze
