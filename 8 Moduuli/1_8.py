import mysql.connector

def hae_lentokentta(icao_koodi):
    yhteys = mysql.connector.connect(
        host='localhost',
        database='lentokentta_tietokanta',
        user='root',
        password='root'
    )
    kursori = yhteys.cursor()
    kysely = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori.execute(kysely, (icao_koodi,))
    tulos = kursori.fetchone()

    if tulos:
        print("Lentokenttä:", tulos[0])
        print("Sijaintikunta:", tulos[1])
    else:
        print("Lentokenttää ei löytynyt.")

    kursori.close()
    yhteys.close()

# Kysytään ICAO-koodi käyttäjältä
icao_koodi = input("Anna ICAO-koodi: ").upper()
hae_lentokentta(icao_koodi)
