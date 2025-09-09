from fastapi import APIRouter, UploadFile, HTTPException
from PIL import Image
from io import BytesIO
import pytesseract
import re
from pdf2image import convert_from_bytes  # for PDF to image conversion

router = APIRouter()

# Example parse function; replace with your full parsing logic
def parse_marksheet_text(text):
    result = {}

    # Candidate details
    name_match = re.search(r"Name\s*[:\-]\s*(.+)", text)
    result['candidate_details'] = {
        "name": {"value": name_match.group(1).strip() if name_match else "", "confidence": 0.9},
        # Add dob, exam_year similarly if present
    }

    # Subjects and marks
    subject_pattern = r"(\w+)\s+(\d+)"
    subjects = re.findall(subject_pattern, text)
    result['subject_marks'] = []
    for subj, marks in subjects:
        result['subject_marks'].append({
            "subject": subj,
            "max_marks": "100",        # assuming max marks 100
            "obtained_marks": marks,
            "grade": "",               # optional, can add later
            "confidence": 0.9
        })

    # Overall result
    result['overall_result'] = {
        "result": {"value": "Pass", "confidence": 0.9},
        "division": {"value": "", "confidence": 0.9}
    }

    # Issue date
    date_match = re.search(r"Date\s*[:\-]\s*(\d{2}[-/]\d{2}[-/]\d{4})", text)
    result['issue_date'] = {"value": date_match.group(1) if date_match else "", "confidence": 0.85}

    return result

@router.post("/extract")
async def extract_marksheet(file: UploadFile):
    # Validate file type
    if file.content_type not in ["image/jpeg", "image/jpg", "application/pdf"]:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    contents = await file.read()

    images = []
    try:
        if file.content_type == "application/pdf":
            # Convert PDF pages to images
            images = convert_from_bytes(contents)
        else:
            images = [Image.open(BytesIO(contents))]

        # OCR each image
        extracted_text = ""
        for img in images:
            extracted_text += pytesseract.image_to_string(img) + "\n"

        # Parse text into structured JSON
        result = parse_marksheet_text(extracted_text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR failed: {str(e)}")

    return result
