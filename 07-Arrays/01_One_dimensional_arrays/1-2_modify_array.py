###
# Modifies array values and prints the array after each change
#
arr = [1, 2, 3, 4, 5]                         # tworzymy listę
print('Array:', arr)                          # wypisujemy listę przed zmianami

arr[0] = arr[0] - 1                           # od pierwszego elementu odejmujemy 1 i zapisujemy go z powrotem
print('Array:', arr)                          # [0, 2, 3, 4, 5]

arr[len(arr) - 1] = arr[len(arr) - 1] + 4     # ostatni element zwiększamy o 4
print('Array:', arr)                          # [0, 2, 3, 4, 9]

arr[len(arr) // 2] = arr[len(arr) // 2] * 2   # środkowy element mnożymy przez 2
print('Array:', arr)                          # [0, 2, 6, 4, 9]
