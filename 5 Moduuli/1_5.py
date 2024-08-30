import random

#Käyttäjältä kysytään arpakuutioiden lukumäärä
lkm = int(input("Kuinka monta arpakuutiota heitetään? "))

summa = 0

#Heitetään arpakuutiota ja lasketaan summa
for _ in range(lkm):
    silmaluku = random.randint(1, 6)  #Arvotaan luku väliltä 1-6
    summa += silmaluku  #Lisätään silmäluku summaan

print(f"Silmälukujen summa on: {summa}")
