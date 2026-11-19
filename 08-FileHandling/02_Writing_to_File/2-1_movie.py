# Program to write movie details to a text file

# Variables containing movie details
movie_title = "Inception"                                   # tytuł filmu
director = "Christopher Nolan"                              # reżyser
lead_actor = "Leonardo DiCaprio"                            # główny aktor

# Name of the file to write to
file_name = 'movie_details.txt'                             # nazwa pliku, który powstanie

# Writing movie details to the file
with open(file_name, 'w') as file:                          # 'w' (write) tworzy plik do zapisu; jeśli już jest, kasuje jego treść
    file.write(f"Movie Title: {movie_title}\n")             # write() zapisuje tekst do pliku; \n przechodzi do nowej linii
    file.write(f"Director: {director}\n")                   # zapisujemy reżysera
    file.write(f"Lead Actor: {lead_actor}\n")               # zapisujemy aktora

print(f"Movie details have been written to {file_name}.")   # informujemy, że zapis się udał
