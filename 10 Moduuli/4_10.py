import random

class Auto:
    def __init__(self, nimi):
        self.nimi = nimi
        self.matka = 0

    def kulje(self):
        nopeus_muutos = random.randint(-5, 5)
        self.matka += max(0, 60 + nopeus_muutos)

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"\nKilpailun '{self.nimi}' tilanne:")
        print(f"{'Auto':<15}{'Matka (km)':<15}")
        print("-" * 30)
        for auto in self.autot:
            print(f"{auto.nimi:<15}{auto.matka:<15.2f}")

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus for auto in self.autot)

# Pääohjelma
def main():
    autot = [Auto(f"Auto {i+1}") for i in range(10)]
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunti += 1
        if tunti % 10 == 0:
            kilpailu.tulosta_tilanne()

    kilpailu.tulosta_tilanne()
    print("Kilpailu on ohi!")

# Suorita pääohjelma
if __name__ == "__main__":
    main()
