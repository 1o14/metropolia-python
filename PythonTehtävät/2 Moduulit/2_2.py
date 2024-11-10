import math

#Kysyy ympyrän säteen
sade = float(input("Anna ympyrän säde: "))

#Laskee ympyrän pinta-alan
pinta_ala = math.pi * sade * sade

print("Ympyrän pinta-ala on: ", round(pinta_ala, 2))
