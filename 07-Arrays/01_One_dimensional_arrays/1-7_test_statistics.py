###
# Prints test statistics
#
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]                                                                    # True = dobra odpowiedź, False = zła

# calculates the number of test questions
question_number = len(test_results)                                  # liczba pytań to liczba elementów listy

# calculates the number of correct answers
correct_answers = 0                                                  # licznik dobrych odpowiedzi, na początku 0
for answer in test_results:                                          # pętla: bierzemy po kolei każdą odpowiedź
    if answer == True:                                               # jeśli odpowiedź jest dobra
        correct_answers = correct_answers + 1                        # zwiększamy licznik o 1

# calculates the number of incorrect answers
incorrect_answers = question_number - correct_answers                # złe odpowiedzi to wszystkie minus dobre

# calculates the percentage of correct answers
percentage = correct_answers / question_number * 100                 # procent = dobre / wszystkie * 100

print('TEST STATISTICS')                                             # nagłówek
print('===============')                                             # linia pod nagłówkiem
print('Number of questions:', question_number)                       # wypisujemy liczbę pytań (15)
print('Number of correct answers:', correct_answers)                 # dobre odpowiedzi (10)
print('Number of incorrect answers:', incorrect_answers)             # złe odpowiedzi (5)
print('Percentage of correct answers:', round(percentage, 2), '%')   # round(..., 2) zaokrągla do 2 miejsc po kropce
