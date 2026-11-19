###
# Draws a square using the draw_square() function
# from the figures module
#
import figures                 # dołączamy nasz plik figures.py
import turtle                  # dołączamy moduł turtle (potrzebny do okna)

# Set up the screen
window = turtle.Screen()       # tworzymy okno do rysowania
window.bgcolor("lightgreen")   # ustawiamy jasnozielone tło

# Use the turtle from the figures module
pen = figures.pen              # bierzemy żółwia z pliku figures, żeby był tylko jeden żółw
pen.speed(5)                   # ustawiamy szybkość rysowania

# Draw a square
figures.draw_square(100)       # rysujemy kwadrat o boku 100

# Hide the turtle and finish
pen.hideturtle()               # chowamy żółwia po rysowaniu
window.mainloop()              # okno zostaje otwarte, dopóki go nie zamkniesz
