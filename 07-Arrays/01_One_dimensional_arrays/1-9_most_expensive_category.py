###
# Calculates which expense category was the most expensive
#
categories = ["Food", "Transport", "Rent", "Entertainment"]    # nazwy kategorii
expenses = [500, 150, 1000, 200]                               # wydatki; ten sam indeks = ta sama kategoria

max_index = 0                                                  # indeks największego wydatku; na początku zakładamy, że to pierwszy
for i in range(1, len(expenses)):                              # sprawdzamy pozostałe wydatki (od indeksu 1)
    if expenses[i] > expenses[max_index]:                      # jeśli ten wydatek jest większy od dotychczas największego
        max_index = i                                          # zapamiętujemy jego indeks

print('The most expensive category:', categories[max_index])   # nazwa kategorii o tym samym indeksie (Rent)
print('Amount:', expenses[max_index])                          # jej kwota (1000)
