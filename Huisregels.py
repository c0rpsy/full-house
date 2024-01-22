huisregels = ["Volg de aanwijzingen van het personeel op.",
    "Houd gangen en nooduitgangen vrij.",
    "Geen eten of drinken meenemen in de collegezalen.",
    "Zet je mobiele telefoon op stil tijdens presentaties.",
    "Respecteer de sprekers en medebezoekers.",
    "Gebruik de daarvoor bestemde prullenbakken.",
    "Fotografeer alleen met toestemming van de sprekers.",
    "Meld verdachte situaties bij het personeel.",
    "Roken is alleen toegestaan op aangewezen plekken.",
    "Houd rekening met medebezoekers en gedraag je respectvol."]

def voeg_huisregel_toe(regel):
    huisregels.append(regel)
    print(f'Huisregel "{regel}" toegevoegd.')

def wijzig_huisregel(regel_nummer, nieuwe_regel):
    if 1 <= regel_nummer <= len(huisregels):
        huisregels[regel_nummer - 1] = nieuwe_regel
        print(f'Huisregel {regel_nummer} gewijzigd naar "{nieuwe_regel}".')

def verwijder_huisregel(regel_nummer):
    if 1 <= regel_nummer <= len(huisregels):
        verwijderde_regel = huisregels.pop(regel_nummer - 1)
        print(f'Huisregel {regel_nummer} verwijderd: "{verwijderde_regel}".')

def bekijk_huisregels():
    print("Huidige huisregels:")
    for nummer, regel in enumerate(huisregels, start=1):
        print(f"{nummer}. {regel}")

# Voorbeeldgebruik:
#voeg_huisregel_toe("Geen roken in het gebouw.")
#bekijk_huisregels()
#wijzig_huisregel(1, "Roken is alleen toegestaan op aangewezen plekken.")
#verwijder_huisregel(2)


bekijk_huisregels()
