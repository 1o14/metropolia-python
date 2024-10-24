class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, tavoitekerros):
        if 0 <= hissin_numero < len(self.hissit):
            self.hissit[hissin_numero].siirry_kerrokseen(tavoitekerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)

if __name__ == "__main__":
    talo = Talo(1, 10, 3)
    talo.aja_hissiä(0, 5)
    talo.palohälytys()
