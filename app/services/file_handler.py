from pdf2image import convert_from_bytes
from PIL import Image
import io
import pytesseract

def validate_and_read_file(file_bytes, content_type):
    images = []

    if content_type == "application/pdf":
        images = convert_from_bytes(file_bytes)  # Convert each PDF page into an image
    else:
        image = Image.open(io.BytesIO(file_bytes))
        images = [image]

    full_text = ""
    for img in images:
        text = pytesseract.image_to_string(img)  # OCR text extraction
        full_text += text + "\n"

    return full_text
