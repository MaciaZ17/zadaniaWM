###
# Dochód rodziny na osobę (z użyciem f-stringów).
#
father_income = 5450                                           # dochód ojca
mother_income = 4920                                           # dochód matki
family_members = 5                                             # liczba członków rodziny
total_income = father_income + mother_income                   # łączny dochód rodziny (10370)
income_per_person = total_income / family_members              # dochód na osobę (2074.0)
print(f'Total family income is {total_income}, and income per person is {income_per_person:.2f}')
# :.2f w klamrach oznacza: wypisz liczbę zmiennoprzecinkową z 2 miejscami po przecinku
