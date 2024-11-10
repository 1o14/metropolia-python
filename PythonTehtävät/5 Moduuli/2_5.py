luvut = []

#Kysytään lukuja, kunnes käyttäjä syöttää tyhjän merkkijonon
while True:
    syote = input("Syötä luku (tai jätä tyhjäksi lopettaaksesi): ")
    if syote == "":  #Tarkistetaan, onko syöte tyhjä
        break  #Lopetetaan syötteen kysyminen
    luvut.append(int(syote))  #Muutetaan syöte luvuksi ja lisätään listaan

#Lajitellaan lista suurimmasta pienimpään
luvut.sort(reverse=True)

print("Viisi suurinta lukua ovat:", luvut[:5])
