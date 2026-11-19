###
# Finds the maximum and minimum number without built-in functions
#
arr = [-15, 8, -31, 47, -2, 19]   # lista liczb

max_value = arr[0]                # na początku zakładamy, że pierwszy element jest największy
min_value = arr[0]                # i że jest najmniejszy
for value in arr:                 # bierzemy po kolei każdy element
    if value > max_value:         # jeśli jest większy od dotychczas największego
        max_value = value         # zapamiętujemy go jako największy
    if value < min_value:         # jeśli jest mniejszy od dotychczas najmniejszego
        min_value = value         # zapamiętujemy go jako najmniejszy

print('Maximum:', max_value)      # wypisujemy największą (47)
print('Minimum:', min_value)      # wypisujemy najmniejszą (-31)
