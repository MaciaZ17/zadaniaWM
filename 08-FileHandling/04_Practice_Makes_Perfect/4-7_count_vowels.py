###
# Calculates the number of vowels in the text entered from the keyboard
#
import re                                    # moduł do wyrażeń regularnych

text = input('Enter text: ')                 # wczytujemy tekst z klawiatury
vowels = re.findall(r'[aeiouAEIOU]', text)   # [aeiouAEIOU] pasuje do jednej samogłoski; findall zbiera wszystkie
print('Number of vowels:', len(vowels))      # liczba samogłosek = długość listy
