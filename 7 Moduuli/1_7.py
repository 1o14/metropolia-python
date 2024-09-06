# Määritellään kuukausien vuodenajat
vuodenajat = {
    1: "Talvi", 2: "Talvi", 3: "Kevät",
    4: "Kevät", 5: "Kevät", 6: "Kesä",
    7: "Kesä", 8: "Kesä", 9: "Syksy",
    10: "Syksy", 11: "Syksy", 12: "Talvi"
}

# Kysytään käyttäjältä kuukauden numero
kuukausi = int(input("Anna kuukauden numero (1-12): "))

# Tulostetaan vuoden aika
print(vuodenajat.get(kuukausi, "Virheellinen kuukauden numero."))
