###
# Function that returns the full name of a day of the week
# based on its number
#
def day_name(day_number):                                # tworzymy funkcję; day_number to numer dnia od 1 do 7
    result = ''                                          # pusta zmienna, wpiszemy do niej nazwę dnia
    if day_number == 1:                                  # jeśli numer to 1 (== porównuje, = przypisuje)
        result = 'Monday'                                # to poniedziałek
    elif day_number == 2:                                # w przeciwnym razie, jeśli 2
        result = 'Tuesday'                               # to wtorek
    elif day_number == 3:                                # jeśli 3
        result = 'Wednesday'                             # to środa
    elif day_number == 4:                                # jeśli 4
        result = 'Thursday'                              # to czwartek
    elif day_number == 5:                                # jeśli 5
        result = 'Friday'                                # to piątek
    elif day_number == 6:                                # jeśli 6
        result = 'Saturday'                              # to sobota
    elif day_number == 7:                                # jeśli 7
        result = 'Sunday'                                # to niedziela
    else:                                                # jeśli numer jest inny niż 1-7
        result = 'Unknown day'                           # nie ma takiego dnia
    return result                                        # funkcja oddaje nazwę dnia

# Function usage
print('The name of day 5 in the week is', day_name(5))   # uruchamiamy funkcję dla 5 i wypisujemy wynik (Friday)
print('The name of day 3 in the week is', day_name(3))   # dla 3 (Wednesday)
print('The name of day 7 in the week is', day_name(7))   # dla 7 (Sunday)
