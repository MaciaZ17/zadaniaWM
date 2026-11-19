###
# Calculates the total value of money spent
#
import re                                               # moduł do wyrażeń regularnych

# file name with shopping report
email_file = 'report.txt'                               # plik z mailem

# read the content of email
with open(email_file, 'r', encoding='utf-8') as file:   # encoding='utf-8' pozwala poprawnie odczytać znak €
    email = file.read()                                 # wczytujemy cały mail jako jeden napis

# regular expression pattern
# for amounts
pattern = r'€\s?(\d+\.?\d*)'                            # znak €, ewentualna spacja, cyfry, ewentualna kropka i dalsze cyfry; w () to, co chcemy dostać

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)                    # lista znalezionych kwot jako napisy, np. ['45.20', '89.99', ...]

# calculate the total purchases
total = 0                                               # suma wydatków, na początku 0
for amount in amounts:                                  # pętla: bierzemy po kolei każdą kwotę
    total = total + float(amount)                       # float() zamienia napis na liczbę z kropką, dodajemy do sumy

# print result
print('Amounts found:', amounts)                        # wypisujemy znalezione kwoty
print('Total money spent: €' + str(round(total, 2)))    # wypisujemy sumę zaokrągloną do groszy (163.49)
