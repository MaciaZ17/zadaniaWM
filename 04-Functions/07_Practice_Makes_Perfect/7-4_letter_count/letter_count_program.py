###
# Checks how many times the letter 'e' appears in a text
#
import letter_counter                                                 # dołączamy nasz plik letter_counter.py

def main():                                                           # program główny
    text = 'You never get a second chance to make a first impression'  # tekst z zadania
    letter = 'e'                                                      # litera, której szukamy
    result = letter_counter.count_letter(text, letter)                # liczymy, ile razy litera jest w tekście
    print(text)                                                       # wypisujemy tekst
    print(f"The number of letter '{letter}':", result)                # wypisujemy wynik (7)

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
