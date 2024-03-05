import qrcode

# Function to create a QR code
def create_qr_code(data, file_name="qrcode.png"):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(file_name)

if __name__ == "__main__":
    # Get user input for the data to encode
    data_to_encode = input("Enter the data to encode in the QR code: ")
    
    # Replace 'my_qrcode.png' with your desired file name
    create_qr_code(data_to_encode, "my_qrcode.png")

    print("QR code generated successfully.")
