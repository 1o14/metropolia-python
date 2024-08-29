import random

# Kysy käyttäjältä pisteiden määrä
pisteiden_maara = int(input("Kuinka monta pistettä arvotaan? "))

ympyra_pisteet = 0  # Lasketaan ympyrän sisällä olevat pisteet

for _ in range(pisteiden_maara):
    x = random.uniform(-1, 1)  # Arvotaan x-koordinaatti
    y = random.uniform(-1, 1)  # Arvotaan y-koordinaatti

    # Tarkistetaan, onko piste ympyrässä
    if x ** 2 + y ** 2 < 1:
        ympyra_pisteet += 1  # Lisää laskuriin

# Laske piin likiarvo
pi_likiarvo = 4 * ympyra_pisteet / pisteiden_maara

print(f"Piin likiarvo on noin {pi_likiarvo}")
