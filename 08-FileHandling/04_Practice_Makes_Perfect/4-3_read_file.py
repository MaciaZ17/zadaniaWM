###
# Tries to print the contents of a file that is not on the disk
# (the program stops with an error)
#
file_name = 'missing_file.txt'       # takiego pliku nie ma na dysku

with open(file_name, 'r') as file:   # tu program się zatrzyma z błędem FileNotFoundError
    print(file.read())               # ta linijka się nie wykona

print('End of program')              # ta też nie, bo program już się zatrzymał
