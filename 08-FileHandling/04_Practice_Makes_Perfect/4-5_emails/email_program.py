###
# Prints the sender, recipient, subject and body of an email
#
import emails                                       # dołączamy nasz plik emails.py

def main():                                         # program główny
    print('Sender:', emails.email_sender())         # adres nadawcy
    print('Recipient:', emails.email_recipient())   # adres odbiorcy
    print('Subject:', emails.email_subject())       # temat
    print('Body:')                                  # podpis
    print(emails.email_body())                      # treść maila

if __name__ == "__main__":                          # prawdziwe, gdy uruchamiasz ten plik (np. przyciskiem Run)
    main()                                          # wtedy uruchamiamy program główny
