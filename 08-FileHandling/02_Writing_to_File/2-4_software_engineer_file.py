###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'              # plik z wszystkimi pracownikami
position_file = 'software_engineer.txt'        # plik, do którego zapiszemy wybranych

# Position
job_title = 'Software Engineer'                # stanowisko, którego szukamy

# write selected employees to a file
with open(employees_file, 'r') as source:      # otwieramy plik z pracownikami do odczytu
    with open(position_file, 'w') as target:   # i jednocześnie plik wynikowy do zapisu
        for line in source:                    # pętla: bierzemy po kolei każdą linię
            if job_title in line:              # jeśli w linii jest szukane stanowisko
                target.write(line)             # zapisujemy całą linię (ma już na końcu znak nowej linii)

print('Saved to', position_file)               # informujemy, że zapis się udał
