###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
# Przypadek 1: brak premii (odpowiedź N)       -> 5000.0
# Przypadek 2: premia 30% (bonus = 0.30, odp. Y) -> 6500.0
#
basic_salary = 5000                                          # podstawowa pensja
total_salary = 0                                             # miejsce na pensję końcową (na razie 0)
bonus = 0.30                                                 # premia 30% zapisana jako ułamek (0.15 = 15%); zmień na 0.15 dla premii 15%
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'   # porównanie daje True, gdy wpisano Y, inaczej False

if is_bonus:                                                 # jeśli pracownik dostaje premię
    total_salary = basic_salary + basic_salary * bonus       # pensja podstawowa + premia (procent od pensji podstawowej)
else:                                                        # jeśli nie dostaje premii
    total_salary = basic_salary                              # pensja to tylko podstawa

print(f'Basic salary: {basic_salary}')                       # wypisujemy pensję podstawową
print(f'Bonus included? {is_bonus}')                         # wypisujemy True/False - czy uwzględniono premię
print(f'Total salary: {total_salary}')                       # wypisujemy pensję końcową
