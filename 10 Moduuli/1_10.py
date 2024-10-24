class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, tavoitekerros):
        while self.kerros < tavoitekerros:
            self.kerros_ylös()
        while self.kerros > tavoitekerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi on kerroksessa {self.kerros}")

if __name__ == "__main__":
    hissi = Hissi(1, 10)
    hissi.siirry_kerrokseen(5)
    hissi.siirry_kerrokseen(1)
