import json

def haal_huisregels():
    try:
        with open('huisregels.json', 'r') as json_bestand:
            data = json.load(json_bestand)
            return data.get('regels', [])
    except FileNotFoundError:
        print("Het opgegeven JSON-bestand is niet gevonden.")
        return []

if __name__ == "__main__":
    huisregels = haal_huisregels()

    if huisregels:
        print("Huisregels:")
        for regel in huisregels:
            print(f"- {regel}")
    else:
        print("Geen huisregels gevonden.")
