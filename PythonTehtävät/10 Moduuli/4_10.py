class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"Kilpailu: {self.nimi}")
        for auto in self.autot:
            print(f"{auto.nimi}: {auto.kilometrit} km")

    def kilpailu_ohi(self):
        return any(auto.kilometrit >= self.pituus for auto in self.autot)

if __name__ == "__main__":
    autot = [Auto(f"Auto {i+1}") for i in range(10)]
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    for tunti in range(10):
        kilpailu.tunti_kuluu()
        kilpailu.tulosta_tilanne()
        if kilpailu.kilpailu_ohi():
            print("Kilpailu on ohi!")
            break

    kilpailu.tulosta_tilanne()  # Tulostaa tilanteen kilpailun päätyttyä
