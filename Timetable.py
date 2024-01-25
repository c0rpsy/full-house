import json

def haal_timetable_op():
    try:
        with open('timetable.json', 'r') as json_bestand:
            data = json.load(json_bestand)
            return data.get('schema', [])
    except FileNotFoundError:
        print("Het opgegeven JSON-bestand is niet gevonden.")
        return []

if __name__ == "__main__":
    timetable = haal_timetable_op()

    if timetable:
        print("Timetable:")
        for sessie in timetable:
            print(f"Tijdslot: {sessie['tijdslot']}, Lokaal: {sessie['sessie']['Lokaal']}, Presentatie: {sessie['sessie']['Presentatie']}")
    else:
        print("Geen timetable gevonden.")
