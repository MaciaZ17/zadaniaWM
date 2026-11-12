###
# Simple calculator
# Asks the user to enter two numbers and a symbol of mathematical operation (+, -, *, /)
# and returns the result.
# Testy: 2 + 3, 2 * 4, 3 - 5, 5 * 6
#
number1 = float(input('Enter first number: '))               # pierwsza liczba (float, żeby działały też ułamki)
number2 = float(input('Enter second number: '))              # druga liczba
operator = input('Enter operator (+, -, *, /): ')            # symbol działania jako tekst

if operator == '+':                                          # dodawanie
    result = number1 + number2                               # liczymy sumę
elif operator == '-':                                        # odejmowanie
    result = number1 - number2                               # liczymy różnicę
elif operator == '*':                                        # mnożenie
    result = number1 * number2                               # liczymy iloczyn
elif operator == '/':                                        # dzielenie
    if number2 == 0:                                         # dzielenia przez zero nie wolno wykonać (błąd programu)
        result = 'division by zero is not possible'          # zamiast liczby zapisujemy komunikat
    else:                                                    # dzielnik jest różny od zera
        result = number1 / number2                           # liczymy iloraz
else:                                                        # nieznany symbol działania
    result = 'unknown operator'                              # zapisujemy komunikat błędu

# print result
print(f'{number1} {operator} {number2} = {result}')          # wypisujemy działanie i wynik
