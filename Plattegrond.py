from PIL import Image

def toon_plattegrond(foto_path):
    # Open de afbeelding met Pillow
    plattegrond = Image.open(foto_path)

    # Toon de afbeelding
    plattegrond.show()

# Bij foto_pad = vul je bestand naam in
foto_pad = 'eventmap.jpg'
toon_plattegrond(foto_pad)
