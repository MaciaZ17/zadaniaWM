###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'                  # plik, który kopiujemy
target_file = 'copy_healthy_lifestyle.txt'               # plik, który powstanie (kopia)

# read the content of the original file
with open(original_file, 'r') as source:                 # otwieramy oryginał do odczytu
    content = source.read()                              # wczytujemy całą jego treść

# write the content to the target file (copy)
with open(target_file, 'w') as target:                   # otwieramy kopię do zapisu
    target.write(content)                                # zapisujemy do niej całą treść

print('File', original_file, 'copied to', target_file)   # informujemy, że kopia jest gotowa
