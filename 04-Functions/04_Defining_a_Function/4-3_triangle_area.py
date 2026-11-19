###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math                                                           # dołączamy moduł math, bo potrzebujemy pierwiastka

# Boki muszą tworzyć trójkąt, inaczej program pokaże błąd.
def triangle_area(a, b, c):                                           # tworzymy funkcję liczącą pole; a, b, c to długości boków
    s = (a + b + c) / 2                                               # liczymy połowę obwodu, bo wymaga tego wzór Herona
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))                 # wzór Herona: pierwiastek z s*(s-a)*(s-b)*(s-c)
    return area                                                       # funkcja oddaje policzone pole

# Triangle sides read from the keyboard
side_a = float(input('Enter side a: '))                               # wczytujemy bok a; float() zamienia napis na liczbę, np. 2.5
side_b = float(input('Enter side b: '))                               # wczytujemy bok b
side_c = float(input('Enter side c: '))                               # wczytujemy bok c
user_area = triangle_area(side_a, side_b, side_c)                     # liczymy pole dla boków, które wpisałeś
print('The area of a triangle with sides', side_a, side_b, side_c, 'is', user_area)  # wypisujemy boki i pole

# Test data
print('The area of a triangle with sides 3, 4, 5 is', triangle_area(3, 4, 5))  # liczymy i od razu wypisujemy pole (6)
print('The area of a triangle with sides 5, 12, 13 is', triangle_area(5, 12, 13))  # powinno wyjść 30
print('The area of a triangle with sides 7, 24, 25 is', triangle_area(7, 24, 25))  # powinno wyjść 84
