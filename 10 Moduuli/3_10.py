class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.current_kerros = alin_kerros

    def siirry_kerrokseen(self, target_kerros):
        if target_kerros < self.alin_kerros or target_kerros > self.ylin_kerros:
            print("Virhe: Kohdekerros ei sallituissa rajoissa.")
            return
        while self.current_kerros < target_kerros:
            self.kerros_ylös()
        while self.current_kerros > target_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.current_kerros < self.ylin_kerros:
            self.current_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.current_kerros}")

    def kerros_alas(self):
        if self.current_kerros > self.alin_kerros:
            self.current_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.current_kerros}")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lukumaara)]

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virheellinen hissin numero.")

    def palohälytys(self):
        print("Palohälytys! Kaikki hissit siirtyvät pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)


# Pääohjelma
talo = Talo(1, 10, 3)  # Talo, jossa 3 hissiä, alimman kerroksen numero 1 ja ylimmän 10

# Ajetaan hissiä
talo.aja_hissiä(0, 5)  # Hissi 0 kerrokseen 5
talo.aja_hissiä(1, 3)  # Hissi 1 kerrokseen 3
talo.aja_hissiä(2, 8)  # Hissi 2 kerrokseen 8

# Palohälytys
talo.palohälytys()  # Kaikki hissit pohjakerrokseen
