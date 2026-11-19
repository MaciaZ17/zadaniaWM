###
# Combines two contact lists and removes duplicates
#
contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}  # pierwsza lista kontaktów
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}  # druga lista kontaktów

merged_contacts = contacts_A | contacts_B                             # suma (|): wszystkie adresy z obu zbiorów, bez powtórek
print("Merged contacts:", merged_contacts)                            # bob@example.com pojawi się tylko raz
