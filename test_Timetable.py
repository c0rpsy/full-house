from Timetable import *

from unittest.mock import mock_open, patch

def test_haal_timetable_op_exists():
    # Met de patch-functie wordt de open-functie vervangen door een mock die vooraf gedefinieerde gegevens retourneert.
    # Hiermee simuleren we het bestaan van het JSON-bestand.
    with patch('builtins.open', new_callable=mock_open, read_data='{"schema": [{"tijdslot": "09:00-10:00", "sessie": {"Lokaal": "A1", "Presentatie": "Introductie"}}]}'), \
         patch('os.path.isfile', return_value=True):

        # Roep de functie aan die het tijdschema ophaalt
        timetable = haal_timetable_op()

    # Controleer of het tijdschema correct is opgehaald
    assert len(timetable) == 1
    assert timetable[0]['tijdslot'] == "09:00-10:00"
    assert timetable[0]['sessie']['Lokaal'] == "A1"
    assert timetable[0]['sessie']['Presentatie'] == "Introductie"

def test_haal_timetable_op_file_not_found():
    # Met de patch-functie wordt de open-functie vervangen door een mock die een FileNotFoundError simuleert.
    # Hiermee simuleren we het ontbreken van het JSON-bestand.
    with patch('builtins.open', side_effect=FileNotFoundError):

        # Roep de functie aan die het tijdschema ophaalt
        timetable = haal_timetable_op()

    # Controleer of de functie correct reageert op een niet-gevonden JSON-bestand
    assert timetable == []

if __name__ == '__main__':
    test_haal_timetable_op_exists()
    test_haal_timetable_op_file_not_found()
