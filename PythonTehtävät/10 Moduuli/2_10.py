class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros  # Hissi aloittaa alimmaisesta kerroksesta

    def siirry_kerrokseen(self, kohdekerros):
        while self.kerros < kohdekerros:
            self.kerros_ylös()
        while self.kerros > kohdekerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi on nyt kerroksessa {self.kerros}.")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros}.")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, tavoitekerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero + 1} kerrokseen {tavoitekerros}.")
            self.hissit[hissin_numero].siirry_kerrokseen(tavoitekerros)

# Testaa Talo-luokkaa
if __name__ == "__main__":
    talo = Talo(1, 10, 3)
    talo.aja_hissiä(0, 5)  # Ajetaan hissiä 1 kerrokseen 5
    talo.aja_hissiä(0, 1)  # Ajetaan hissiä takaisin alimmaiseen kerrokseen
