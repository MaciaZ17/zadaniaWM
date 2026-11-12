###
# Calculates the sum of even numbers from 1 to a given number N
# (wersja z pętlą while zamiast for)
#
N = 10                                                       # górna granica
sum_even = 0                                                 # suma liczb parzystych
i = 1                                                        # while nie tworzy licznika sam, więc robimy go ręcznie

# Calculate the sum of even numbers
while i <= N:                                                # odpowiednik range(1, N + 1)
    if i % 2 == 0:                                           # czy i jest parzyste
        sum_even += i                                        # dodajemy do sumy
    i += 1                                                   # zwiększamy licznik (konieczne, inaczej pętla nigdy się nie skończy)

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")   # wynik: 30
