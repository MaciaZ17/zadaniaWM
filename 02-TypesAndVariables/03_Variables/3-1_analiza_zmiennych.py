###
# Analiza programu ze zmiennymi: w programie jest 7 zmiennych.
# Nazwa               Wartość          Typ
# company             "ABC Data"       str
# phone               "555-123-009"    str   (to tekst, bo jest w cudzysłowie i ma myślniki)
# employees           25               int
# remote_work         True             bool
# big_company         False            bool  (25 > 100 jest fałszem)
# income              4500000          int
# income_per_person   180000.0         float (dzielenie / zawsze daje float)
#
company = "ABC Data"                        # zmienna tekstowa z nazwą firmy
phone = "555-123-009"                       # numer telefonu jako tekst
employees = 25                              # liczba pracowników (int)
remote_work = True                          # czy jest praca zdalna (bool)
big_company = employees > 100               # porównanie 25 > 100 daje False
income = 4500000                            # dochód firmy (int)
income_per_person = income / employees      # dochód na osobę: 4500000 / 25 = 180000.0
print(company, type(company))               # wypisujemy wartość i typ każdej zmiennej
print(phone, type(phone))                   # str
print(employees, type(employees))           # int
print(remote_work, type(remote_work))       # bool
print(big_company, type(big_company))       # bool
print(income, type(income))                 # int
print(income_per_person, type(income_per_person))  # float
