import mysql.connector

def hae_lentokentat(maakoodi):
    yhteys = mysql.connector.connect(
        host='localhost',
        database='lentokentta_tietokanta',
        user='root',
        password='root'
    )
    kursori = yhteys.cursor()

    kysely = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"
    kursori.execute(kysely, (maakoodi.upper(),))

    for tyyppi, maara in kursori:
        print(f"{tyyppi}: {maara} kpl")

    kursori.close()
    yhteys.close()

maakoodi = input("Anna maakoodi (esim. FI): ")
hae_lentokentat(maakoodi)
