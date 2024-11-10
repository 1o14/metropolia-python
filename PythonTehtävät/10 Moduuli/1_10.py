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

# Testaa Hissi-luokkaa
if __name__ == "__main__":
    hissi = Hissi(1, 10)
    hissi.siirry_kerrokseen(5)
    hissi.siirry_kerrokseen(1)  # Siirrytään takaisin alimmaiseen kerrokseen
