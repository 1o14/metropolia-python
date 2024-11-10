nimet = set()

while True:
    # Kysy käyttäjältä nimi
    nimi = input("Anna nimi (tyhjällä syötteellä lopetetaan): ")

    # Tarkista, onko syöte tyhjää
    if nimi == "":
        break

    # Tarkista, onko nimi jo joukossa
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

# Tulosta kaikki syötetyt nimet
print("\nSyötetyt nimet:")
for nimi in nimet:
    print(nimi)
