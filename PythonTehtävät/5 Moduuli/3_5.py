#Kysytään käyttäjältä kokonaisluku
luku = int(input("Syötä kokonaisluku: "))

#Oletetaan aluksi, että luku on alkuluku
on_alkuluku = True

#Tarkistetaan, onko luku suurempi kuin 1 (alkuluvut ovat suurempia kuin 1)
if luku > 1:
    #Käydään läpi kaikki luvut 2:sta lukuun asti
    for i in range(2, luku):
        if luku % i == 0:  #Jos luku jakautuu tasan jollain luvulla
            on_alkuluku = False  #Luku ei ole alkuluku
            break  #Lopetetaan tarkistaminen, koska löytyi jakaja
else:
    on_alkuluku = False  #Luvut, jotka ovat 1 tai pienempiä, eivät ole alkulukuja

#Tulostetaan tulos
if on_alkuluku:
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")
