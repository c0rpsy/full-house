from Huisregels import *

import unittest
from unittest.mock import mock_open, patch

def test_haal_huisregels_exists():
    # Met de patch-functie wordt de open-functie vervangen door een mock die vooraf gedefinieerde gegevens retourneert.
    # Hiermee simuleren we het bestaan van het JSON-bestand.
    with patch('builtins.open', new_callable=mock_open, read_data='{"regels": ["Regel 1", "Regel 2"]}'), \
         patch('os.path.isfile', return_value=True):

        # Roep de functie aan die de huisregels ophaalt
        huisregels = haal_huisregels()

    # Vergelijk de geretourneerde huisregels met de verwachte waarden
    assert huisregels == ["Regel 1", "Regel 2"]

def test_haal_huisregels_file_not_found():
    # Met de patch-functie wordt de open-functie vervangen door een mock die een FileNotFoundError simuleert.
    # Hiermee simuleren we het ontbreken van het JSON-bestand.
    with patch('builtins.open', side_effect=FileNotFoundError):

        # Roep de functie aan die de huisregels ophaalt
        huisregels = haal_huisregels()

    # Controleer of de functie correct reageert op een niet-gevonden JSON-bestand
    assert huisregels == []
