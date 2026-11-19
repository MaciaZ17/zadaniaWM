###
# Draws a square - the original program from the instructions
# (before moving the code into a function)
#
import turtle                  # dołączamy moduł turtle do rysowania

# Set up the screen
window = turtle.Screen()       # tworzymy okno do rysowania
window.bgcolor("lightgreen")   # ustawiamy jasnozielone tło

# Create the turtle
pen = turtle.Turtle()          # tworzymy żółwia, który rysuje (pen = pisak)
pen.speed(5)                   # ustawiamy szybkość rysowania (od 1 do 10)

# Side length
side_length = 100              # długość boku kwadratu

# Draw a square
for i in range(4):             # powtarzamy 4 razy, bo kwadrat ma 4 boki
    pen.forward(side_length)   # żółw idzie do przodu i rysuje bok
    pen.right(90)              # żółw skręca w prawo o 90 stopni

# Hide the turtle and finish
pen.hideturtle()               # chowamy żółwia po rysowaniu
window.mainloop()              # okno zostaje otwarte, dopóki go nie zamkniesz
