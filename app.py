import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# Set the page configuration
st.set_page_config(page_title="QR Code Generator with Logo", layout="centered")

# Neumorphism-style CSS for input and button styling
st.markdown("""
    <style>
    body {
        background-color: #000000;
    }
    .stTextInput>div>input {
        font-weight: bold;
        background: #333333;
        border: none;
        color: white;
        padding: 10px;
        box-shadow: inset 5px 5px 10px #1a1a1a, inset -5px -5px 10px #4d4d4d;
    }
    .stButton>button {
        font-weight: bold;
        color: white;
        background: #333333;
        border: none;
        padding: 10px 20px;
        box-shadow: 5px 5px 10px #1a1a1a, -5px -5px 10px #4d4d4d;
    }
    h1 {
        font-family: Arial, sans-serif;
        font-weight: bold;
        color: white;
        text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# Main heading
st.title("QR Code Generator with Logo")

# Input field to enter the URL
url = st.text_input("Enter the URL you want to encode:", "")

# Checkbox to choose whether to upload a logo
add_logo = st.checkbox("Add a logo to the QR code?")

# Upload field for logo if the checkbox is checked
logo_file = None
if add_logo:
    logo_file = st.file_uploader("Upload your logo (PNG format):", type=['png'])

# Button to generate the QR code
if st.button("Generate QR Code"):
    if url:
        # Create QR code with high error correction
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Generate QR code image
        qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')

        if add_logo and logo_file:
            # Load the logo
            logo = Image.open(logo_file)

            # Calculate the size and position for the logo, including padding
            qr_width, qr_height = qr_img.size
            logo_size = qr_width // 4  # Logo takes up 1/4th of the QR code
            logo.thumbnail((logo_size, logo_size), Image.LANCZOS)  # Resize logo

            # Padding (you can adjust padding here)
            padding = 20  # Padding around the logo
            logo_size_with_padding = logo_size + padding

            # Create a white rectangle for logo background with padding
            logo_background = Image.new('RGB', (logo_size_with_padding, logo_size_with_padding), (255, 255, 255))

            # Paste the logo onto the center of the rectangle
            logo_background.paste(logo, (padding // 2, padding // 2), mask=logo if logo.mode == 'RGBA' else None)

            # Calculate the position where the logo background will be placed
            logo_position = ((qr_width - logo_size_with_padding) // 2, (qr_height - logo_size_with_padding) // 2)

            # Paste the logo background with padding onto the QR code
            qr_img.paste(logo_background, logo_position)

        # Resize the QR code to 1000x1000 pixels
        qr_img = qr_img.resize((1000, 1000), Image.LANCZOS)

        # Convert the image to display on Streamlit
        buffer = BytesIO()
        qr_img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()

        # Display the QR code
        st.image(img_bytes)

        # Provide a download button
        st.download_button(label="Download QR Code", data=img_bytes, file_name="qr_code.png", mime="image/png")
    else:
        st.error("Please enter a URL.")