###
# Functions for drawing figures with the turtle module
#
import turtle                             # dołączamy moduł turtle do rysowania
import math                               # dołączamy moduł math, bo potrzebujemy pierwiastka

pen = turtle.Turtle()                     # tworzymy żółwia, którego używają funkcje z tego pliku

###
# Draw a square
#
def draw_square(length):                  # funkcja rysuje kwadrat; length to długość boku
    for i in range(4):                    # powtarzamy 4 razy, bo kwadrat ma 4 boki
        pen.forward(length)               # rysujemy bok
        pen.right(90)                     # skręcamy w prawo o 90 stopni

###
# Draw an isosceles triangle (two equal sides and a right angle)
# W treści jest nazwa draw_trangle (literówka), tu jest poprawiona.
#
def draw_triangle(length):                # funkcja rysuje trójkąt; length to długość dwóch równych boków
    hypotenuse = length * math.sqrt(2)    # liczymy najdłuższy bok (z twierdzenia Pitagorasa)
    pen.forward(length)                   # rysujemy pierwszy równy bok
    pen.left(135)                         # skręcamy w lewo o 135 stopni
    pen.forward(hypotenuse)               # rysujemy najdłuższy bok
    pen.left(135)                         # znowu skręcamy w lewo o 135 stopni
    pen.forward(length)                   # rysujemy drugi równy bok
    pen.left(90)                          # skręcamy, żeby żółw patrzył tam, gdzie na początku

###
# Draw a rectangle with sides a and b
# W treści jest "lenght" (literówka), tu jest "length".
#
def draw_rectangle(length_a, length_b):   # funkcja rysuje prostokąt o bokach a i b
    for i in range(2):                    # powtarzamy 2 razy: bok a, bok b, bok a, bok b
        pen.forward(length_a)             # rysujemy bok a
        pen.right(90)                     # skręcamy w prawo o 90 stopni
        pen.forward(length_b)             # rysujemy bok b
        pen.right(90)                     # skręcamy w prawo o 90 stopni
