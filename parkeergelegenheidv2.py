import json

class Parkeerbeheerder:
    def __init__(self):
        self.parkeer_data = self.laad_parkeerinformatie()

    def laad_parkeerinformatie(self):
        try:
            with open('parkeerv2.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def sla_parkeerinformatie_op(self):
        with open('parkeerv2.json', 'w') as file:
            json.dump(self.parkeer_data, file)

    def voeg_parkeerplaats_toe(self, plaats, beschikbare_plekken):
        self.parkeer_data.append({"plaats": plaats, "beschikbare_plekken": beschikbare_plekken})
        self.sla_parkeerinformatie_op()

    def wijzig_parkeerplaats(self, plaats, nieuwe_beschikbare_plekken):
        for info in self.parkeer_data:
            if info["plaats"] == plaats:
                info["beschikbare_plekken"] = nieuwe_beschikbare_plekken
                self.sla_parkeerinformatie_op()
                print(f"Informatie voor {plaats} is gewijzigd naar {nieuwe_beschikbare_plekken} beschikbare plekken.")
                return

        print(f"Plaats {plaats} niet gevonden. Wijziging mislukt.")

    def verwijder_parkeerplaats(self, plaats):
        for info in self.parkeer_data:
            if info["plaats"] == plaats:
                self.parkeer_data.remove(info)
                self.sla_parkeerinformatie_op()
                print(f"Informatie voor {plaats} is verwijderd.")
                return

        print(f"Plaats {plaats} niet gevonden. Verwijdering mislukt.")

    def krijg_parkeerinformatie(self):
        return self.parkeer_data

if __name__ == "__main__":
    parkeer_manager = Parkeerbeheerder()

    doorgaan = True

    while doorgaan:
        commando = input("Voer een commando in ('parkeer info' om parkeerinformatie te tonen, 'toevoegen' om een nieuwe plaats toe te voegen, 'wijzigen' om informatie te wijzigen, 'verwijderen' om een plaats te verwijderen, 'stop' om te stoppen): ")

        if commando.lower() == 'parkeer info':
            parkeer_informatie = parkeer_manager.krijg_parkeerinformatie()
            print("Parkeerinformatie:")
            for info in parkeer_informatie:
                print(f"Plaats: {info['plaats']}, Beschikbare plekken: {info['beschikbare_plekken']}")
        elif commando.lower() == 'wijzigen':
            plaats = input("Voer de naam van de plaats in: ")
            nieuwe_beschikbare_plekken = int(input("Voer het nieuwe aantal beschikbare plekken in: "))
            parkeer_manager.wijzig_parkeerplaats(plaats, nieuwe_beschikbare_plekken)
        elif commando.lower() == 'toevoegen':
            plaats = input("Voer de naam van de nieuwe plaats in: ")
            beschikbare_plekken = int(input("Voer het aantal beschikbare plekken in: "))
            parkeer_manager.voeg_parkeerplaats_toe(plaats, beschikbare_plekken)
        elif commando.lower() == 'verwijderen':
            plaats = input("Voer de naam van de plaats in die je wilt verwijderen: ")
            parkeer_manager.verwijder_parkeerplaats(plaats)
        elif commando.lower() == 'stop':
            doorgaan = False
        else:
            print("Ongeldig commando. Probeer opnieuw.")
