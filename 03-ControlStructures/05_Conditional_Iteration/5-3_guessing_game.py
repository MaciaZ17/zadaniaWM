###
# A simple number guessing game
#
import random                                                # moduł do losowania liczb

# Randomly chosen number to be guessed from 1 to 100
number_to_guess = random.randint(1, 100)                     # komputer losuje liczbę z zakresu 1-100
user_guess = 0                                               # zmyślona wartość startowa, żeby wejść do pętli

print("Guess the number between 1 and 100!")                 # informacja dla gracza

while user_guess != number_to_guess:                         # pętla trwa, dopóki gracz nie trafi
    user_guess = int(input("Enter your guess: "))            # wczytujemy propozycję gracza

    if user_guess < number_to_guess:                         # propozycja mniejsza niż wylosowana
        print("Too low! Try again.")                         # podpowiedź: za mało
    elif user_guess > number_to_guess:                       # propozycja większa niż wylosowana
        print("Too high! Try again.")                        # podpowiedź: za dużo
    else:                                                    # propozycja równa wylosowanej
        print("Congratulations! You guessed the correct number.")   # gratulacje; po tym warunek pętli stanie się fałszywy
