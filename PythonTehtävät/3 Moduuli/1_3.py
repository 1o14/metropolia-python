#Käyttäjältä kysytään kuhan pituus
pituus = int(input("Anna kuhan pituus senttimetreinä: "))

# Tarkistetaan, onko kuha alamittainen
if pituus < 37:
    puuttuu = 37 - pituus
    print(f"Kuha on alamittainen. Laske se takaisin järveen. Kuha on {puuttuu} cm liian lyhyt.")
else:
    print("Kuha on tarpeeksi suuri.")
