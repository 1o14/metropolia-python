def gallonat_to_litrat(gallonat):
    #Muuntaa gallonat litroiksi (1 gallona = 3.785 litraa)
    return gallonat * 3.785

while True:
    #Kysytään käyttäjältä bensiinin määrä gallonina
    gallonat = float(input("Anna bensiinin määrä gallonina (negatiivinen luku lopettaa): "))

    #Tarkistetaan, onko syöte negatiivinen
    if gallonat < 0:
        break  #Lopetetaan ohjelma, jos syöte on negatiivinen

    #Lasketaan litrat ja tulostetaan tulos
    print(f"{gallonat} gallonaa on {gallonat_to_litrat(gallonat):.2f} litraa.")
