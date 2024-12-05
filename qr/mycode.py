import qrcode
import base64

# Step 1: Read the HTML file
with open("index.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

# Step 2: Encode the HTML content as a Data URI
encoded_html = base64.b64encode(html_content.encode("utf-8")).decode("utf-8")
data_uri = f"data:text/html;charset=UTF-8;base64,{encoded_html}"

# Step 3: Generate the QR code
qr = qrcode.QRCode(
    version=40,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data_uri)
qr.make(fit=True)

# Step 4: Customize and save the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")
qr_image.save("qr_code_no_host.png")

print("QR code generated and saved as 'qr_code_no_host.png'")
from PIL import Image

# Add logo to the QR code
qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")
try:
    logo = Image.open("mohd.jpeg")  # Replace 'logo.png' with your logo file
    logo_size = (60, 60)
    logo = logo.resize(logo_size)

    # Position logo at the center of the QR code
    logo_position = ((qr_image.size[0] - logo_size[0]) // 2, (qr_image.size[1] - logo_size[1]) // 2)
    qr_image.paste(logo, logo_position)
except FileNotFoundError:
    print("Logo not found. QR code created without a logo.")

# Save the QR code with the logo
qr_image.save("qr_code_with_logo_no_host.png")
