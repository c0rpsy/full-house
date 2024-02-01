from parkeergelegenheidv2 import *

import unittest
from unittest.mock import mock_open, patch

def test_parkeer_manager_operations():
    # Gebruik een patch om de bestandstoegang te vervangen door een mock
    with patch('builtins.open', new_callable=mock_open, read_data='[]'):
        # Initialiseer de Parkeerbeheerder
        parkeer_manager = Parkeerbeheerder()

        # Voeg een parkeerplaats toe
        parkeer_manager.voeg_parkeerplaats_toe("P1", 10)

        # Controleer of de toegevoegde parkeerplaats aanwezig is
        parkeer_info = parkeer_manager.krijg_parkeerinformatie()
        assert len(parkeer_info) == 1
        assert parkeer_info[0]["plaats"] == "P1"
        assert parkeer_info[0]["beschikbare_plekken"] == 10

        # Wijzig het aantal beschikbare plekken
        parkeer_manager.wijzig_parkeerplaats("P1", 5)

        # Controleer of de wijziging is doorgevoerd
        parkeer_info = parkeer_manager.krijg_parkeerinformatie()
        assert parkeer_info[0]["beschikbare_plekken"] == 5

        # Verwijder de parkeerplaats
        parkeer_manager.verwijder_parkeerplaats("P1")

        # Controleer of de parkeerplaats is verwijderd
        parkeer_info = parkeer_manager.krijg_parkeerinformatie()
        assert len(parkeer_info) == 0

if __name__ == '__main__':
    test_parkeer_manager_operations()
