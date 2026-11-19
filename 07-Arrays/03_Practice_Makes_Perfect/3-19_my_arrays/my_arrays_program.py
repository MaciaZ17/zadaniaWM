###
# Uses the MyArrays module for the sequence 7,3,8,5,2
#
import MyArrays                                                       # dołączamy nasz plik MyArrays.py

def main():                                                           # program główny
    numbers = [7, 3, 8, 5, 2]                                         # lista liczb z zadania
    print('Numbers: 7,3,8,5,2')                                       # wypisujemy liczby
    print('Second largest number:', MyArrays.second_largest(numbers))  # druga największa (7)
    print('Largest - smallest:', MyArrays.difference(numbers))        # różnica największej i najmniejszej (6)
    print('Median:', MyArrays.median(numbers))                        # mediana (5)
    smallest_largest = MyArrays.min_max(numbers)                      # lista [najmniejsza, największa]
    print(f'Smallest and largest number: {smallest_largest[0]},{smallest_largest[1]}')  # wypisujemy 2,8
    print('Numbers as a string:', MyArrays.to_string(numbers))        # wypisujemy 7-3-8-5-2

if __name__ == "__main__":                                            # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                                            # wtedy uruchamiamy program główny
