###
# Manages a queue of files to print
#
import queue                                                          # dołączamy moduł queue

# creates a queue of files to print
files_to_print = queue.Queue()                                        # pusta kolejka plików do druku

while True:                                                           # pętla działa, dopóki nie wybierzemy 0
    print('1. Add file to print')                                     # opcje menu
    print('2. Print file')                                            # kolejna opcja menu
    print('0. Quit')                                                  # kolejna opcja menu
    menu = input('Select an option: ')                                # wczytujemy wybór

    if menu == '1':                                                   # dodanie pliku
        file_name = input('Enter file name to print: ')               # wczytujemy nazwę pliku
        files_to_print.put(file_name)                                 # dodajemy plik na koniec kolejki
        print(f'File {file_name} added. Files in queue: {files_to_print.qsize()}')  # informujemy, ile plików czeka

    elif menu == '2':                                                 # drukowanie
        if not files_to_print.empty():                                # jeśli kolejka nie jest pusta
            file_to_print = files_to_print.get()                      # zabieramy pierwszy plik z kolejki
            print(f'File {file_to_print} is currently being printed. Please wait!')  # informujemy o druku
        else:                                                         # jeśli kolejka jest pusta
            print('There are no files to print.')                     # informujemy, że nie ma czego drukować

    elif menu == '0':                                                 # wyjście
        break                                                         # kończymy pętlę

    else:                                                             # inna odpowiedź
        print('Unknown option.')                                      # informujemy o złym wyborze
