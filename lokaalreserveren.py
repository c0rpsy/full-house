class LokaalReserveringSysteem:
    def __init__(self):
        self.beschikbare_lokalen = {
            'b.3.301': {'reserveringen': set(), 'informatie': None},
            'b.3.302': {'reserveringen': set(), 'informatie': None},
            'b.3.303': {'reserveringen': set(), 'informatie': None},
            'b.3.304': {'reserveringen': set(), 'informatie': None},
            'b.3.305': {'reserveringen': set(), 'informatie': None},
            'b.3.306': {'reserveringen': set(), 'informatie': None},
            'b.3.307': {'reserveringen': set(), 'informatie': None},
            'b.3.308': {'reserveringen': set(), 'informatie': None},
            'b.3.309': {'reserveringen': set(), 'informatie': None},
            'b.3.310': {'reserveringen': set(), 'informatie': None},
        }
        self.gereserveerde_lokalen = set()

    def opslaan(self):
        with open("lokalen.json", "w") as f:
            for lokaal, info in self.beschikbare_lokalen.items():
                reserveringen = ", ".join(info['reserveringen'])
                f.write(f"{lokaal}:{reserveringen}:{info['informatie']}\n")

    def laden(self):
        try:
            with open("lokalen.json", "r") as f:
                for line in f:
                    lokaal, reserveringen, informatie = line.strip().split(":")
                    self.beschikbare_lokalen[lokaal]['reserveringen'] = set(reserveringen.split(", ")) if reserveringen else set()
                    self.beschikbare_lokalen[lokaal]['informatie'] = informatie if informatie != "None" else None
                    if lokaal in self.beschikbare_lokalen and lokaal not in self.gereserveerde_lokalen and self.beschikbare_lokalen[lokaal]['reserveringen']:
                        self.gereserveerde_lokalen.add(lokaal)

        except FileNotFoundError:
            pass

    def reserveer_lokaal(self, lokaal, informatie=None):
        if lokaal in self.beschikbare_lokalen:
            if lokaal not in self.gereserveerde_lokalen:
                self.gereserveerde_lokalen.add(lokaal)
                self.beschikbare_lokalen[lokaal]['reserveringen'].add(informatie)
                self.beschikbare_lokalen[lokaal]['informatie'] = informatie
                print(f"Lokaal {lokaal} succesvol gereserveerd met informatie: {informatie}.")
                self.opslaan()  # Sla de wijzigingen op
                return True
            else:
                print(f"Lokaal {lokaal} is al gereserveerd. Dubbele reservering is niet toegestaan.")
                return False
        else:
            print(f"Lokaal {lokaal} is niet beschikbaar of al gereserveerd.")
            return False

    def wijzig_lokaal(self, lokaal, informatie):
        if lokaal in self.gereserveerde_lokalen:
            self.beschikbare_lokalen[lokaal]['informatie'] = informatie
            print(f"Informatie voor gereserveerd lokaal {lokaal} succesvol gewijzigd naar: {informatie}.")
            self.opslaan()  # Sla de wijzigingen op
            return True
        else:
            print(f"Lokaal {lokaal} is niet gereserveerd of niet bekend.")
            return False

    def verwijder_lokaal(self, lokaal):
        if lokaal in self.gereserveerde_lokalen:
            self.gereserveerde_lokalen.remove(lokaal)
            self.beschikbare_lokalen[lokaal]['reserveringen'] = set()
            self.beschikbare_lokalen[lokaal]['informatie'] = None
            self.opslaan()  # Sla de wijzigingen op
            print(f"Lokaal {lokaal} succesvol verwijderd.")
            return True
        else:
            print(f"Lokaal {lokaal} is niet gereserveerd of niet bekend.")
            return False

    def toon_beschikbare_lokalen(self):
        print("Beschikbare lokalen:")
        for lokaal, info in self.beschikbare_lokalen.items():
            print(f"{lokaal}: {info['reserveringen']}, Informatie: {info['informatie']}")

    def toon_gereserveerde_lokalen(self):
        print("Gereserveerde lokalen:", self.gereserveerde_lokalen)

# Voorbeeldgebruik
lokaal_reservering = LokaalReserveringSysteem()

# Laad de opgeslagen gegevens
lokaal_reservering.laden()

# Loop totdat alle lokalen zijn gekozen
while lokaal_reservering.beschikbare_lokalen:
    # Toon beschikbare lokalen
    lokaal_reservering.toon_beschikbare_lokalen()

    # Geef de gebruiker de keuze om te reserveren, wijzigen, verwijderen of stoppen
    keuze = input("Wil je een lokaal reserveren (R), wijzigen (W), verwijderen (V) of stoppen (S)? ").upper()

    if keuze == 'R':
        # Reserveer een lokaal naar keuze
        gekozen_lokaal = input("Voer het gewenste lokaal in (bijv. b.3.301): ")
        informatie = input("Voer informatie in voor het gereserveerde lokaal: ")
        reservering_succesvol = lokaal_reservering.reserveer_lokaal(gekozen_lokaal, informatie)
    elif keuze == 'W':
        # Wijzig informatie voor een gereserveerd lokaal
        gewijzigd_lokaal = input("Voer het gereserveerde lokaal in dat je wilt wijzigen: ")
        nieuwe_informatie = input("Voer de nieuwe informatie in: ")
        wijziging_succesvol = lokaal_reservering.wijzig_lokaal(gewijzigd_lokaal, nieuwe_informatie)
    elif keuze == 'V':
        # Verwijder een gereserveerd lokaal
        te_verwijderen_lokaal = input("Voer het gereserveerde lokaal in dat je wilt verwijderen: ")
        verwijdering_succesvol = lokaal_reservering.verwijder_lokaal(te_verwijderen_lokaal)
    elif keuze == 'S':
        break
    else:
        print("Ongeldige keuze. Kies 'R' voor reserveren, 'W' voor wijzigen, 'V' voor verwijderen, of 'S' voor stoppen.")

# Toon de eindstatus van beschikbare en gereserveerde lokalen
lokaal_reservering.toon_beschikbare_lokalen()
lokaal_reservering.toon_gereserveerde_lokalen()

# Controleer of het reserveringsproces succesvol is afgerond
if not lokaal_reservering.beschikbare_lokalen:
    print("Alle lokalen zijn succesvol gereserveerd. Reserveringsproces afgerond.")
else:
    print("Reserveringsproces geannuleerd.")
