###
# Module with a function that returns a month name
# based on the month number
#
def month(n):                    # funkcja zwraca nazwę miesiąca; n to numer od 1 do 12
    name = ''                    # pusta zmienna, wpiszemy do niej nazwę
    if n == 1:                   # jeśli numer to 1
        name = 'January'         # to styczeń
    elif n == 2:                 # jeśli 2
        name = 'February'        # to luty
    elif n == 3:                 # jeśli 3
        name = 'March'           # to marzec
    elif n == 4:                 # jeśli 4
        name = 'April'           # to kwiecień
    elif n == 5:                 # jeśli 5
        name = 'May'             # to maj
    elif n == 6:                 # jeśli 6
        name = 'June'            # to czerwiec
    elif n == 7:                 # jeśli 7
        name = 'July'            # to lipiec
    elif n == 8:                 # jeśli 8
        name = 'August'          # to sierpień
    elif n == 9:                 # jeśli 9
        name = 'September'       # to wrzesień
    elif n == 10:                # jeśli 10
        name = 'October'         # to październik
    elif n == 11:                # jeśli 11
        name = 'November'        # to listopad
    elif n == 12:                # jeśli 12
        name = 'December'        # to grudzień
    else:                        # jeśli numer jest inny niż 1-12
        name = 'Unknown month'   # nie ma takiego miesiąca
    return name                  # funkcja oddaje nazwę

if __name__ == "__main__":       # prawdziwe tylko, gdy uruchamiasz months.py bezpośrednio
    print(month(7))              # szybki test: powinno wypisać July
