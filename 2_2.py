import math

#Kysy ympyrän säde
sade = float(input("Anna ympyrän säde: "))

#Laske ympyrän pinta-ala
pinta_ala = math.pi * sade * sade

print("Ympyrän pinta-ala on: ", round(pinta_ala, 2))
