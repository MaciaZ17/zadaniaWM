###
# Functions for drawing figures with the turtle module
#
import turtle                 # dołączamy moduł turtle do rysowania

pen = turtle.Turtle()         # tworzymy żółwia, którego używają funkcje z tego pliku

###
# Draw a square
#
def draw_square(length):      # funkcja rysuje kwadrat; length to długość boku
    for i in range(4):        # powtarzamy 4 razy, bo kwadrat ma 4 boki
        pen.forward(length)   # żółw idzie do przodu i rysuje bok
        pen.right(90)         # żółw skręca w prawo o 90 stopni
