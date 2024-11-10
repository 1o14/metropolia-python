import random

oikea_luku = random.randint(1, 10)  # Arvotaan luku väliltä 1..10

while True:
    arvaus = int(input("Arvaa luku väliltä 1-10: "))

    if arvaus > oikea_luku:
        print("Liian suuri arvaus")
    elif arvaus < oikea_luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein!")
        break  # Lopetetaan peli, kun arvaus on oikea
