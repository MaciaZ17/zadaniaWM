###
# Uses the MyText module for a sample sentence
#
import MyText                                                         # dołączamy nasz plik MyText.py

def main():                                                           # program główny
    text = 'An apple a day keeps the doctor away'                     # tekst z zadania
    print('Text:', text)                                              # wypisujemy tekst
    print('Number of words:', MyText.word_count(text))                # liczba słów (8)
    print('Words from the longest:', ','.join(MyText.words_by_length(text)))  # ','.join() skleja słowa z listy przecinkami
    print('Words ordered alphabetically:', ','.join(MyText.words_alphabetically(text)))  # słowa alfabetycznie

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
