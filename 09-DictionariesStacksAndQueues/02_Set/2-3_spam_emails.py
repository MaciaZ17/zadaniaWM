###
# Displays received email addresses that are on the spam list
#
emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}  # odebrane maile
spam_list = {"spam1@example.com", "spam2@example.com"}                # lista spamu

spam_emails = emails_received & spam_list                             # część wspólna (&): adresy, które są w obu zbiorach
print("Spam emails:", spam_emails)                                    # wypisujemy spam
