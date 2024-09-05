import math

# Funktio yksikköhinnan laskemiseen
def laske_yksikkohinta(halkaisija, hinta):
    pinta_ala = math.pi * (halkaisija / 2) ** 2
    return hinta / (pinta_ala / 10000)  # Muutetaan neliömetrit euroiksi

# Pääohjelma
halkaisija1 = float(input("Ensimmäisen pizzan halkaisija cm: "))
hinta1 = float(input("Ensimmäisen pizzan hinta euroina: "))
halkaisija2 = float(input("Toisen pizzan halkaisija cm: "))
hinta2 = float(input("Toisen pizzan hinta euroina: "))

yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza on edullisempi per neliömetri.")
else:
    print("Toinen pizza on edullisempi per neliömetri.")