import random

def heita_noppaa():
    #Heittää noppaa ja palauttaa silmäluvun väliltä 1-6
    return random.randint(1, 6)

silmaluku = 0

#Jatketaan nopan heittoa niin kauan kunnes tulee kuutonen
while silmaluku != 6:
    silmaluku = heita_noppaa()  #Heitetään noppaa
    print(silmaluku)
