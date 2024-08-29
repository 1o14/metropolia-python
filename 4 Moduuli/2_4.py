# Käytetään while-loopia, joka jatkuu, kunnes käyttäjä syöttää negatiivisen arvon
while True:
    tuumat = float(input("Anna tuumamäärä (negatiivinen arvo lopettaa): "))

    if tuumat < 0:
        break  # Lopetetaan ohjelma, jos tuumamäärä on negatiivinen

    # Muunnetaan tuumat senttimetreiksi
    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {senttimetrit} senttimetriä")
