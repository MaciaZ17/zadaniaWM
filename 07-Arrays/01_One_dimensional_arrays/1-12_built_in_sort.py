###
# Sorts data using the built-in function sorted()
#
# Sort the data from lowest to highest value
distances_traveled = [120, 150, 180, 90, 200, 175, 160]               # przejechane odległości
print(sorted(distances_traveled))                                     # sorted() układa od najmniejszej do największej

# Sort the data in descending order, from highest to lowest value
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]         # temperatury
print(sorted(daily_temperatures, reverse=True))                       # reverse=True odwraca kolejność: od największej

# Sort the data in ascending order
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
              "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]  # nazwy plików
print(sorted(file_names))                                             # napisy sorted() układa alfabetycznie
