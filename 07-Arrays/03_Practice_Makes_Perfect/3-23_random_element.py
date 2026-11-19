###
# Prints a few randomly selected array elements
#
import random                                                         # dołączamy moduł random do losowania

def rand_elem(array):                                                 # funkcja zwraca losowy element listy
    index = random.randint(0, len(array) - 1)                         # losujemy indeks od 0 do ostatniego
    return array[index]                                               # oddajemy element o tym indeksie

def main():                                                           # program główny
    fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']  # lista owoców
    for i in range(5):                                                # powtarzamy 5 razy
        print(rand_elem(fruits))                                      # wypisujemy losowy owoc

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
