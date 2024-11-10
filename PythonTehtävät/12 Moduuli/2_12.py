import requests


def hae_saa(paikkakunta, api_key):
    # API-osoite sään hakemiseen
    url = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}&units=metric"

    try:
        # Tehdään GET-pyyntö API:lle
        response = requests.get(url)

        # Tarkistetaan, että pyyntö onnistui
        if response.status_code == 200:
            data = response.json()  # Muutetaan JSON-muotoiseksi
            saateksti = data['weather'][0]['description']  # Sään kuvaus
            lampotila = data['main']['temp']  # Lämpötila Celsius-asteina
            return saateksti, lampotila
        else:
            return None, "Paikkakuntaa ei löydy."
    except requests.exceptions.RequestException as e:
        return None, f"Virhe yhteydessä: {e}"


# Pääohjelma
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Korvaa omalla API-avaimellasi
    paikkakunta = input("Anna paikkakunnan nimi: ")
    saateksti, lampotila = hae_saa(paikkakunta, api_key)

    if saateksti:
        print(f"Sään kuvaus: {saateksti}")
        print(f"Lämpötila: {lampotila} °C")
    else:
        print(lampotila)
