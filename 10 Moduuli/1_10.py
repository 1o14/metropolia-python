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
            print(f"Hissi on nyt kerroksessa {self.current_kerros}")

    def kerros_alas(self):
        if self.current_kerros > self.alin_kerros:
            self.current_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.current_kerros}")

# Pääohjelma
hissi = Hissi(1, 10)  # Luo hissi, jonka alimman kerroksen numero on 1 ja ylimmän 10
hissi.siirry_kerrokseen(5)  # Siirry viidenteen kerrokseen
hissi.siirry_kerrokseen(1)  # Siirry takaisin alimpaan kerrokseen
