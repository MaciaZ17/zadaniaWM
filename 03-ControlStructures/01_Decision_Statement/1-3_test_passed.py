###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
# Testy: 20 -> zdany, 11 -> zdany, 10 -> zdany, 9 -> niezdany, 0 -> niezdany
#
total_tasks = 20                                             # liczba wszystkich zadań w teście
tasks_ok = int(input('Enter number of correct tasks: '))     # wczytujemy liczbę poprawnych zadań
test_passed = False                                          # na starcie zakładamy, że test niezdany

if tasks_ok >= total_tasks / 2:                              # co najmniej 50% = co najmniej połowa wszystkich zadań (10 z 20)
    test_passed = True                                       # jeśli warunek spełniony, zmieniamy wartość na True

if test_passed:                                              # sprawdzamy zmienną logiczną (nie trzeba pisać == True)
    print('Congratulations! You passed the test.')           # komunikat dla zdanego testu
else:                                                        # w przeciwnym razie
    print('Unfortunately, you failed the test.')             # komunikat dla niezdanego testu
