kaupungit = []

#Kysytään viiden kaupungin nimet käyttäjältä
for i in range(5):
    kaupunki = input(f"Syötä kaupungin {i + 1} nimi: ")
    kaupungit.append(kaupunki)  #Lisätään kaupunki listaan

#Tulostetaan kaupungit allekkain
for kaupunki in kaupungit:
    print(kaupunki)
