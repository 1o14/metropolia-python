class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

# Pääohjelma
auto = Auto("ABC-123", 142)
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print("Nykyinen nopeus:", auto.nopeus, "km/h")

auto.kiihdytä(-200)  # Hätäjarrutus
print("Uusi nopeus hätäjarrutuksen jälkeen:", auto.nopeus, "km/h")
