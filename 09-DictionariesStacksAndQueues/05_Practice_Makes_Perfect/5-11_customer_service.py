###
# Supports customer service in an office using a queue
#
import queue                                                       # dołączamy moduł queue

customers = queue.Queue()                                          # pusta kolejka klientów
next_ticket = 1                                                    # numer następnego biletu

while True:                                                        # pętla działa, dopóki nie wybierzemy 0
    print()                                                        # pusta linia dla czytelności
    print('1. New customer (take a ticket)')                       # opcje menu
    print('2. Serve next customer')                                # kolejna opcja menu
    print('0. Quit')                                               # kolejna opcja menu
    option = input('Select an option: ')                           # wczytujemy wybór

    if option == '1':                                              # nowy klient
        customers.put(next_ticket)                                 # dodajemy jego numer na koniec kolejki
        print('Your ticket number:', next_ticket)                  # wypisujemy numer biletu
        print('People in the queue:', customers.qsize())           # i ile osób czeka
        next_ticket = next_ticket + 1                              # następny klient dostanie kolejny numer
    elif option == '2':                                            # obsługa klienta
        if customers.empty():                                      # jeśli kolejka jest pusta
            print('No customers waiting.')                         # nie ma kogo obsłużyć
        else:                                                      # w przeciwnym razie
            print('Now serving ticket number:', customers.get())   # zabieramy pierwszego z kolejki
    elif option == '0':                                            # wyjście
        break                                                      # kończymy pętlę
    else:                                                          # inna odpowiedź
        print('Unknown option.')                                   # informujemy o złym wyborze
