# Julkaisuluokka, joka toimii perusluokkana
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

# Kirja-aliluokka, joka perii Julkaisu-luokasta
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    # Metodi, joka tulostaa kirjan tiedot
    def tulosta_tiedot(self):
        print(f'Kirja: {self.nimi}\nKirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumäärä}')

# Lehti-aliluokka, joka perii Julkaisu-luokasta
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    # Metodi, joka tulostaa lehden tiedot
    def tulosta_tiedot(self):
        print(f'Lehti: {self.nimi}\nPäätoimittaja: {self.paatoimittaja}')

# Pääohjelma
if __name__ == "__main__":
    # Luodaan julkaisut
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    # Tulostetaan molempien julkaisujen tiedot
    lehti.tulosta_tiedot()
    print()  # Tyhjää riviä erottamaan tulostukset
    kirja.tulosta_tiedot()
