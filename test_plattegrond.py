import pytest
from PIL import Image
from io import StringIO

def toon_plattegrond(foto_path):
    plattegrond = Image.open(foto_path)
    plattegrond.show()

def test_toon_plattegrond(capsys):
    foto_pad = 'eventmap.jpg'

    # Vang de standaarduitvoer op
    with capsys.disabled():
        toon_plattegrond(foto_pad)

    # Hier kun je assertions toevoegen om de uitvoer te controleren als dat nodig is
    # Bijvoorbeeld, assert "Expected output" in captured.out
    # Houd er rekening mee dat de exacte uitvoer mogelijk afhangt van het besturingssysteem en de Pillow-versie.

if __name__ == '__main__':
    pytest.main()
