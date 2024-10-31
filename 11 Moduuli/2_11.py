# Auto-luokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0  # Alkuperäinen nopeus
        self.matkamittari = 0  # Alkuperäinen matkamittarilukema

    # Metodi, joka asettaa halutun nopeuden
    def aseta_nopeus(self, nopeus):
        if 0 <= nopeus <= self.huippunopeus:
            self.nopeus = nopeus
        else:
            print("Nopeus ei voi ylittää huippunopeutta tai olla negatiivinen.")

    # Metodi, joka simuloi ajamista
    def aja(self, tuntia):
        self.matkamittari += self.nopeus * tuntia

# Sähköauto-aliluokka
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

# Polttomoottoriauto-aliluokka
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

# Pääohjelma
if __name__ == "__main__":
    # Luodaan auto-objektit
    sahkoauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    # Asetetaan nopeudet
    sahkoauto.aseta_nopeus(150)
    polttomoottoriauto.aseta_nopeus(160)

    # Ajetaan kolme tuntia
    sahkoauto.aja(3)
    polttomoottoriauto.aja(3)

    # Tulostetaan matkamittarilukemat
    print(f'Sähköauton matkamittarilukema: {sahkoauto.matkamittari} km')
    print(f'Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.matkamittari} km')
