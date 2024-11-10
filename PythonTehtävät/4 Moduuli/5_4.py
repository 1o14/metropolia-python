oikea_tunnus = "miska"
oikea_salasana = "pasi123"

yritykset = 0  # Lasketaan yritysten määrä

while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break  # Lopetetaan ohjelma, kun kirjautuminen onnistuu
    else:
        print("Väärä tunnus tai salasana")
        yritykset += 1  # Kasvatetaan yritysten määrää yhdellä

if yritykset == 5:
    print("Pääsy evätty")
