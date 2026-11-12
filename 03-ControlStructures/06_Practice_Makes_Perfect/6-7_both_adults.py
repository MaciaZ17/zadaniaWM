###
# Checking if both people are adults
#
person1_name = input('Enter first person name: ')            # imię pierwszej osoby
person1_age = int(input('Enter first person age: '))         # wiek pierwszej osoby
person2_name = input('Enter second person name: ')           # imię drugiej osoby
person2_age = int(input('Enter second person age: '))        # wiek drugiej osoby
if person1_age >= 18 and person2_age >= 18:                  # obie osoby muszą mieć co najmniej 18 lat
    print(f'Both {person1_name} and {person2_name} are adults')   # obie dorosłe
else:                                                        # przynajmniej jedna niepełnoletnia
    print(f'Either {person1_name} or {person2_name} is not an adult')   # komunikat
