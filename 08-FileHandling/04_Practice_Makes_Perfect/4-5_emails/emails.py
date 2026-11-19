###
# Module with functions that fetch data from a raw email (email.txt)
#
import re                                                    # moduł do wyrażeń regularnych

def read_email():                                            # funkcja pomocnicza: wczytuje cały plik email.txt
    with open('email.txt', 'r', encoding='utf-8') as file:   # otwieramy plik do odczytu
        return file.read()                                   # oddajemy całą treść maila

def email_sender():                                          # funkcja zwraca adres nadawcy
    email = read_email()                                     # wczytujemy mail
    match = re.search(r'From:.*?([\w.-]+@[\w.-]+)', email)   # szukamy adresu w linii From:; .*? pomija jak najmniej znaków
    return match.group(1)                                    # group(1) oddaje to, co jest w nawiasie (), czyli sam adres

def email_recipient():                                       # funkcja zwraca adres odbiorcy
    email = read_email()                                     # wczytujemy mail
    match = re.search(r'To:.*?([\w.-]+@[\w.-]+)', email)     # to samo dla linii To:
    return match.group(1)                                    # oddajemy sam adres

def email_subject():                                         # funkcja zwraca temat maila
    email = read_email()                                     # wczytujemy mail
    match = re.search(r'Subject: (.*)', email)               # (.*) łapie wszystko do końca linii po Subject:
    return match.group(1)                                    # oddajemy temat

def email_body():                                            # funkcja zwraca treść maila
    email = read_email()                                     # wczytujemy mail
    match = re.search(r'\n\n(.*)', email, re.DOTALL)         # treść zaczyna się po pierwszej pustej linii; DOTALL: kropka łapie też Enter
    return match.group(1).strip()                            # oddajemy treść bez pustych linii na końcu
