###
# Sums numbers entered by user and calculates the arithmetic mean
#
total_sum = 0                                                # suma wpisanych liczb
count = 0                                                    # ile liczb wpisano (potrzebne do średniej)

while True:                                                  # pętla nieskończona, przerwiemy ją przez break
    number = int(input("Enter a number (0 to stop): "))      # wczytujemy liczbę

    if number == 0:                                          # zero oznacza koniec wpisywania
        break                                                # Exit the loop when 0 is entered
    total_sum += number                                      # dodajemy liczbę do sumy
    count += 1                                               # zwiększamy licznik wpisanych liczb

print(f"The total sum of the numbers is: {total_sum}")       # wypisujemy sumę
if count > 0:                                                # średnią liczymy tylko, gdy wpisano choć jedną liczbę (unikamy dzielenia przez 0)
    mean = total_sum / count                                 # średnia arytmetyczna = suma / ilość liczb
    print(f"The arithmetic mean is: {mean:.2f}")             # wypisujemy średnią z 2 miejscami po przecinku
else:                                                        # nie wpisano żadnej liczby
    print("No numbers were entered")                         # komunikat
