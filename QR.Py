import qrcode
from PIL import Image

def generate_qr_code(data):
    # Maak een QR-code-object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Voeg de gegevens toe aan de QR-code
    qr.add_data(data)
    qr.make(fit=True)

    # Maak een afbeelding van de QR-code met de PIL Image-module
    img = qr.make_image(fill_color="black", back_color="white")

    # Toon de QR Code
    img.show()

def process_arrival():
    # Hier kun je logica toevoegen voor het verwerken van de aankomst, zoals het registreren van de aankomsttijd
    print("Aankomst geregistreerd!")

if __name__ == "__main__":
    # Voorbeeldgebruik
    data_to_encode = "https://ih0.redbubble.net/image.1615061405.6202/raf,360x360,075,t,fafafa:ca443f4786.jpg"
    
    # Genereer de QR-code
    generate_qr_code(data_to_encode)
    
    # Toon bericht voor het scannen
    print("Scan de QR-code om je aankomst te registreren.")
    
    # Simuleer het scannen van de QR-code
    input("Druk op Enter nadat de QR-code is gescand.")
    
    # Verwerk de aankomst
    process_arrival()


