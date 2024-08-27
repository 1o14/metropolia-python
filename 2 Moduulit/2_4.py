luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

#Laskee lukujen summan
summa = luku1 + luku2 + luku3

#Laskee lukujen tulon
tulo = luku1 * luku2 * luku3

#Laskee lukujen keskiarvon
keskiarvo = summa / 3

print("Lukujen summa on:", summa)
print("Lukujen tulo on:", tulo)
print("Lukujen keskiarvo on:", round(keskiarvo, 2))