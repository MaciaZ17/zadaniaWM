###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# different than S, M, L, XL)
#
size = input('Enter size symbol: ')                          # wczytujemy symbol rozmiaru jako tekst

if size == 'S':                                              # pierwszy warunek: rozmiar S
    print('S: Small size')                                   # opis rozmiaru S
elif size == 'M':                                            # elif sprawdzany tylko, gdy poprzednie warunki były fałszywe
    print('M: Medium size')                                  # opis rozmiaru M
elif size == 'L':                                            # kolejny warunek
    print('L: Large size')                                   # opis rozmiaru L
elif size == 'XL':                                           # kolejny warunek
    print('XL: Extra large size')                            # opis rozmiaru XL
else:                                                        # żaden z powyższych warunków nie był prawdziwy
    print('Incorrect symbol')                                # komunikat o błędnym symbolu
