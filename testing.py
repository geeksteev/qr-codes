import barcode

# Load QR code image
reader = barcode.barcoderecognition.BarCodeReader("C:\\Files\\Sample_qr.jpg")

# Specify quality settings to read incorrect and tiny QR codes
reader.quality_settings.read_tiny_barcodes = True
reader.quality_settings.allow_incorrect_barcodes = True

# Read QR codes
recognized_results = reader.read_bar_codes()

# Show results
for x in recognized_results:
    print("Code Text: " + x.code_text)
    print("Type: " + x.code_type_name)