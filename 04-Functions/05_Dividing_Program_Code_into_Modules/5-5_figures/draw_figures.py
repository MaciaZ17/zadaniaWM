###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures                    # dołączamy nasz plik figures.py
import turtle                     # dołączamy moduł turtle (potrzebny do okna)

# Set up the screen
window = turtle.Screen()          # tworzymy okno do rysowania
window.bgcolor("lightgreen")      # ustawiamy jasnozielone tło

# Use the turtle from the figures module
pen = figures.pen                 # bierzemy żółwia z pliku figures, żeby był tylko jeden żółw
pen.speed(5)                      # ustawiamy szybkość rysowania

def move_to(x, y):                # funkcja przenosi żółwia w punkt (x, y) bez rysowania
    pen.penup()                   # podnosimy pisak, żeby nie rysował
    pen.goto(x, y)                # przenosimy żółwia; punkt (0, 0) to środek okna
    pen.pendown()                 # opuszczamy pisak, żeby znowu rysował

## Draw figures
move_to(-250, 200)                # idziemy w lewo do góry
figures.draw_square(100)          # rysujemy kwadrat o boku 100
move_to(-250, -50)                # idziemy w lewo na dół
figures.draw_square(60)           # rysujemy mniejszy kwadrat

move_to(-50, 100)                 # idziemy na środek do góry
figures.draw_triangle(100)        # rysujemy trójkąt
move_to(-50, -150)                # idziemy na środek na dół
figures.draw_triangle(60)         # rysujemy mniejszy trójkąt

move_to(150, 200)                 # idziemy w prawo do góry
figures.draw_rectangle(120, 60)   # rysujemy prostokąt 120 na 60
move_to(150, -50)                 # idziemy w prawo na dół
figures.draw_rectangle(60, 100)   # rysujemy prostokąt 60 na 100

# Hide the turtle and finish
pen.hideturtle()                  # chowamy żółwia po rysowaniu
window.mainloop()                 # okno zostaje otwarte, dopóki go nie zamkniesz
