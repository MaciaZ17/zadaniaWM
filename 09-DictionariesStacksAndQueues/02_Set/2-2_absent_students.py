###
# Identifies students who are absent
#
all_students = {"Alice", "John", "Sara", "Bob"}      # wszyscy studenci
attended_students = {"Alice", "Bob"}                 # studenci, którzy przyszli

absent_students = all_students - attended_students   # różnica (-): ci, którzy są w pierwszym zbiorze, a nie ma ich w drugim
print(absent_students)                               # wypisujemy nieobecnych (John i Sara)
