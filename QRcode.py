import qrcode
from datetime import datetime
import os

# Directory to save QR codes
output_dir = "generated_qrcodes"
os.makedirs(output_dir, exist_ok=True)

# Generate a unique filename based on the current timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"qrcode_{timestamp}.png"
filepath = os.path.join(output_dir, filename)

# Data to encode in the QR code
data = input("Enter the data for the QR code: ")

# Create the QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Thickness of the border
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save(filepath)

print(f"QR Code generated and saved as {filepath}")
