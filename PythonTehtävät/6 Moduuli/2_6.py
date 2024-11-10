import random

def heita_noppaa(tahkojen_maara):
    #Heittää noppaa ja palauttaa satunnaisen luvun väliltä 1-tahkojen_maara
    return random.randint(1, tahkojen_maara)

tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))  #Kysytään käyttäjältä nopan tahkojen määrä
silmaluku = 0

#Jatketaan heittoa, kunnes saadaan nopan maksimisilmäluku
while silmaluku != tahkojen_maara:
    silmaluku = heita_noppaa(tahkojen_maara)  #Heitetään noppaa käyttäjän antamalla tahkojen määrällä
    print(silmaluku)
