import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunti):
        self.kuljettu_matka += self.nopeus * tunti

# Pääohjelma
autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_jatkuu = True

while kilpailu_jatkuu:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_jatkuu = False
            break

print("Kilpailun tulokset:")
print(f"{'Rekisteritunnus':<10} {'Huippunopeus':<15} {'Nopeus':<10} {'Kuljettu matka':<15}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<15} {auto.nopeus:<10} {auto.kuljettu_matka:<15}")
