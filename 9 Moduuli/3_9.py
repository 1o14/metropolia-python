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

    def kulje(self, tunti):
        self.kuljettu_matka += self.nopeus * tunti

# Pääohjelma
auto = Auto("ABC-123", 142)
auto.kiihdytä(60)
auto.kulje(1.5)
print("Kuljettu matka:", auto.kuljettu_matka, "km")
