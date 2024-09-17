import mysql.connector
from geopy.distance import geodesic


def hae_koordinaatit(icao):
    yhteys = mysql.connector.connect(
        host='localhost',
        database='lentokentta_tietokanta',
        user='root',
        password='root'
    )
    kursori = yhteys.cursor()

    kysely = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori.execute(kysely, (icao.upper(),))
    tulos = kursori.fetchone()

    kursori.close()
    yhteys.close()

    return tulos  # palauttaa (lat, lon) tuple-muodossa


def laske_etaisyys(icao1, icao2):
    koord1 = hae_koordinaatit(icao1)
    koord2 = hae_koordinaatit(icao2)

    if koord1 and koord2:
        etaisyys = geodesic(koord1, koord2).kilometers
        print(f"Etäisyys lentokenttien {icao1.upper()} ja {icao2.upper()} välillä on {etaisyys:.2f} km.")
    else:
        print("Virhe: Tarkista ICAO-koodit.")


icao1 = input("Anna ensimmäinen ICAO-koodi: ")
icao2 = input("Anna toinen ICAO-koodi: ")
laske_etaisyys(icao1, icao2)
