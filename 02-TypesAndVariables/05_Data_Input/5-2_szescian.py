###
# A program to calculate the volume and surface area of a cube.
# Test: a=4 -> V=64, P=96 ; a=7 -> V=343, P=294
#
cube_side_string = input('Enter cube side: ')      # wczytujemy bok jako tekst
cube_side = int(cube_side_string)                  # zamieniamy tekst na liczbę całkowitą
cube_volume = cube_side ** 3                       # objętość sześcianu: a^3
cube_surface_area = 6 * cube_side ** 2             # pole powierzchni: 6 ścian po a^2
print(f'The volume of a cube with side {cube_side} is {cube_volume}')            # wypisujemy objętość
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')  # wypisujemy pole
