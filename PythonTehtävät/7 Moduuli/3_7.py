# Alustetaan sanakirja lentoasemien tallentamiseen
lentoasemat = {}

while True:
    # Kysy käyttäjältä toiminto
    valinta = input("Valitse toiminto: (1) Lisää lentoasema, (2) Hae lentoasema, (3) Lopeta: ")

    if valinta == "1":
        # Lisää lentoasema
        icao = input("ICAO-koodi: ")
        nimi = input("Lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema lisätty.")

    elif valinta == "2":
        # Hae lentoasema
        icao = input("ICAO-koodi: ")
        nimi = lentoasemat.get(icao, "Lentoasemaa ei löytynyt.")
        print(f"Lentoaseman nimi: {nimi}")

    elif valinta == "3":
        # Lopeta ohjelma
        print("Ohjelma lopetetaan.")
        break

    else:
        # Virheellinen valinta
        print("Virheellinen valinta. Valitse 1, 2 tai 3.")
