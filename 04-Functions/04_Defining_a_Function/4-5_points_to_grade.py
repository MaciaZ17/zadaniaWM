###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):                                             # tworzymy funkcję, która z punktów robi ocenę
    grade = ''                                                        # pusta zmienna, wpiszemy do niej ocenę
    # Sprawdzamy od największego progu: gdyby zacząć od 10, to 20 pkt dałoby Satisfactory.
    if points >= 18:                                                  # jeśli punktów jest 18 lub więcej
        grade = 'Excellent'                                           # ocena: Excellent
    elif points >= 14:                                                # w przeciwnym razie, jeśli 14 lub więcej
        grade = 'Good'                                                # ocena: Good
    elif points >= 10:                                                # w przeciwnym razie, jeśli 10 lub więcej
        grade = 'Satisfactory'                                        # ocena: Satisfactory
    else:                                                             # we wszystkich pozostałych przypadkach (mniej niż 10)
        grade = 'Fail'                                                # ocena: Fail
    return grade                                                      # funkcja oddaje ocenę

test_result = 15                                                      # liczba zdobytych punktów
final_grade = pts_to_grade(test_result)                               # zamieniamy punkty na ocenę
print('You scored', test_result, 'points on the test. Your final grade is', final_grade)  # wypisujemy wynik (Good)
