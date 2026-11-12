###
# Checks whether at least one number entered
# from the keyboard is not negative
#
x = int(input('Enter first number: '))                       # pierwsza liczba
y = int(input('Enter second number: '))                      # druga liczba

if not x < 0 or not y < 0:                                   # not odwraca wynik: "nie jest ujemna" dla x lub dla y
    print(f'At least one of the numbers {x} and {y} is not negative')   # co najmniej jedna nieujemna
else:                                                        # obie ujemne
    print(f'Both numbers {x} and {y} are negative')         # obie ujemne
