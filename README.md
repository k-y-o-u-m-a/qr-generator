# QR Code Generator with Optional Logo

A Streamlit-based web application for generating custom QR codes. Users can create high-resolution QR codes from any URL, with the option to add a custom logo in the center. The QR codes can be downloaded in PNG format at a resolution of 1000x1000 pixels.

## Features

- **Generate Custom QR Codes**: Input any URL to create a QR code.
- **Optional Logo Integration**: Upload a custom logo to be embedded in the center of the QR code.
- **Downloadable PNG**: Generated QR codes are downloadable in high quality.

## Demo

![QR Code Example](example_qr_code.png)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/qr-generator.git
   cd qr-generator
   ```

2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate

   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt

   ```

4. **Usage**

   Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

   Open your browser and navigate to http://localhost:8501.

5. **Generate QR Codes**:

   - Enter a URL in the input box.
   - (Optional) Check the box to upload a logo to be placed in the center of the QR code.
   - Click Generate QR Code to create the QR code.
   - Use the Download QR Code button to save the generated QR code as a PNG file.

6. Dependencies

   - Streamlit: For creating the web interface.
   - qrcode: For generating the QR code.
   - Pillow (PIL): For image manipulation, resizing, and adding a logo.

7. Project Structure

   - app.py: Main application file containing the logic for the QR code generation and UI design.
   - requirements.txt: List of dependencies required to run the app.
