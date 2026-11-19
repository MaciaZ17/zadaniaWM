###
# Prints the number of elements greater than the value entered from the keyboard
#
arr = [3.5, 7.2, 1.8, 9.4, 5.0, 6.6, 2.1]                      # lista liczb rzeczywistych
print('Array:', arr)                                           # wypisujemy listę

value = float(input('Enter a value: '))                        # wczytujemy liczbę; float() pozwala wpisać np. 4.5
count = 0                                                      # licznik, na początku 0
for number in arr:                                             # bierzemy po kolei każdą liczbę
    if number > value:                                         # jeśli jest większa od wpisanej
        count = count + 1                                      # zwiększamy licznik
print('Number of elements greater than', value, 'is', count)   # wypisujemy wynik
