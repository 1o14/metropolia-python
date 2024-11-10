import requests

def hae_chuck_norris_vitsi():
    # API-osoite satunnaisen vitsin hakemiseen
    url = "https://api.chucknorris.io/jokes/random"

    try:
        # Tehdään GET-pyyntö API:lle
        response = requests.get(url)

        # Tarkistetaan, että pyyntö onnistui
        if response.status_code == 200:
            vitsi_data = response.json()  # Muutetaan JSON-muotoiseksi
            return vitsi_data['value']  # Palautetaan vitsin teksti
        else:
            return "Vitsien haku epäonnistui."
    except requests.exceptions.RequestException as e:
        return f"Virhe yhteydessä: {e}"


# Pääohjelma
if __name__ == "__main__":
    vitsi = hae_chuck_norris_vitsi()
    print("Chuck Norris -vitsi:")
    print(vitsi)
