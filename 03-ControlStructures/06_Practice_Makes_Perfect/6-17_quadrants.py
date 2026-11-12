###
# Określa ćwiartkę układu współrzędnych lub oś dla punktu P(x, y).
#
x = int(input('x = '))                                       # współrzędna x
y = int(input('y = '))                                       # współrzędna y

if x == 0 and y == 0:                                        # oba zera
    print('Point P(0,0) is the origin of the coordinate system')   # początek układu
elif x == 0:                                                 # tylko x = 0
    print(f'Point P({x},{y}) is on the Y axis')              # na osi Y
elif y == 0:                                                 # tylko y = 0
    print(f'Point P({x},{y}) is on the X axis')              # na osi X
elif x > 0 and y > 0:                                        # oba dodatnie
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')    # I ćwiartka
elif x < 0 and y > 0:                                        # x ujemne, y dodatnie
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')   # II ćwiartka
elif x < 0 and y < 0:                                        # oba ujemne
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')    # III ćwiartka
else:                                                        # x dodatnie, y ujemne
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')   # IV ćwiartka
