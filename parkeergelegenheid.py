import json

class Parkeerbeheerder:
    def __init__(self):
        self.parkeer_data = self.laad_parkeerinformatie()

    def laad_parkeerinformatie(self):
        try:
            with open('parkeer.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def sla_parkeerinformatie_op(self):
        with open('parkeer.json', 'w') as file:
            json.dump(self.parkeer_data, file)

    def voeg_parkeerplaats_toe(self, plaats, beschikbare_plekken):
        self.parkeer_data.append({"plaats": plaats, "beschikbare_plekken": beschikbare_plekken})
        self.sla_parkeerinformatie_op()

    def krijg_parkeerinformatie(self):
        return self.parkeer_data

if __name__ == "__main__":
    parkeer_manager = Parkeerbeheerder()

    doorgaan = True

    while doorgaan:
        commando = input("Voer een commando in ('parkeer info' om parkeerinformatie te tonen, 'stop' om te stoppen): ")

        if commando.lower() == 'parkeer info':
            parkeer_informatie = parkeer_manager.krijg_parkeerinformatie()
            for info in parkeer_informatie:
                print(f"Plaats: {info['plaats']}, Beschikbare plekken: {info['beschikbare_plekken']}")
        elif commando.lower() == 'stop':
            doorgaan = False
        else:
            print("Ongeldig commando. Probeer opnieuw.")
