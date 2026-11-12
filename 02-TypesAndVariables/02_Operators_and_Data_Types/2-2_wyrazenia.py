###
# Liczba operatorów i argumentów oraz wartości wyrażeń.
# Kolejność działań w Pythonie: ** (najpierw), potem * / // %, potem + -, na końcu porównania.
# Działania o tym samym priorytecie liczymy od lewej do prawej.
#
print(3 * 2 + 1)        # 2 operatory (*, +), 3 argumenty (3,2,1). Najpierw 3*2=6, potem 6+1 = 7
print(5 + 10 * 5)       # 2 operatory (+, *), 3 argumenty. Najpierw 10*5=50, potem 5+50 = 55
print(4 + 4 / 2 ** 2)   # 3 operatory (+, /, **), 4 argumenty. 2**2=4, potem 4/4=1.0, na końcu 4+1.0 = 5.0
print(4 % 3 % 2 % 1)    # 3 operatory (%,%,%), 4 argumenty. Od lewej: 4%3=1, 1%2=1, 1%1 = 0
print(1 + 2 % 3 ** 4 * 5)  # 4 operatory (+, %, **, *), 5 argumentów. 3**4=81, 2%81=2, 2*5=10, 1+10 = 11
print(True != False)    # 1 operator (!=), 2 argumenty. True jest różne od False, więc wynik to True
