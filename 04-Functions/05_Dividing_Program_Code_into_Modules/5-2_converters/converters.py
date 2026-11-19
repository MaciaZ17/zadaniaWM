###
# Functions for converting length units
#
def cm_to_m(cm):                        # funkcja zamienia centymetry na metry
    return cm / 100                     # dzielimy przez 100, bo 1 m = 100 cm

def m_to_cm(m):                         # funkcja zamienia metry na centymetry
    return m * 100                      # mnożymy przez 100

def cm_to_inches(cm):                   # nowa funkcja: centymetry na cale
    return cm / 2.54                    # dzielimy przez 2.54, bo 1 cal = 2.54 cm

def feet_inches_to_cm(feet, inches):    # nowa funkcja: stopy i cale na centymetry
    total_inches = feet * 12 + inches   # zamieniamy stopy na cale (1 stopa = 12 cali) i dodajemy resztę cali
    return total_inches * 2.54          # zamieniamy cale na centymetry
