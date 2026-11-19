###
# Removes duplicate email addresses
#
# Zbiór (set) przechowuje tylko różne elementy, bez powtórek i bez stałej kolejności.
emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]  # lista z powtórzonym adresem
unique_emails = set(emails)                                           # set() zamienia listę na zbiór, więc powtórki znikają
print(unique_emails)                                                  # wypisujemy zbiór (kolejność może być za każdym razem inna)
