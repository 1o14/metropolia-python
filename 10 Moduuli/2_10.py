class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.current_kerros = alin_kerros

    def siirry_kerrokseen(self, target_kerros):
        while self.current_kerros < target_kerros:
            self.kerros_ylös()
        while self.current_kerros > target_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.current_kerros < self.ylin_kerros:
            self.current_kerros += 1

    def kerros_alas(self):
        if self.current_kerros > self.alin_kerros:
            self.current_kerros -= 1


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lukumaara)]

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
            print(f"Hissi {hissin_numero} on nyt kerroksessa {self.hissit[hissin_numero].current_kerros}")
        else:
            print("Virheellinen hissin numero.")


# Pääohjelma
talo = Talo(1, 10, 3)  # Luo talo, jossa on 3 hissiä, alimman kerroksen numero 1 ja ylimmän 10

# Ajetaan hissiä
talo.aja_hissiä(0, 5)  # Siirry hissillä 0 kerrokseen 5
talo.aja_hissiä(1, 3)  # Siirry hissillä 1 kerrokseen 3
talo.aja_hissiä(2, 8)  # Siirry hissillä 2 kerrokseen 8
talo.aja_hissiä(0, 1)  # Siirry takaisin hissillä 0 alimpaan kerrokseen
