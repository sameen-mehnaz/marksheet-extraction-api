Marksheet Extraction API – Approach Note

Project Overview
The Marksheet Extraction API allows uploading images or PDFs of mark sheets and returns structured JSON with candidate details, subject marks, overall result, and issue date. It supports both images and multi-page PDFs and provides confidence scores for extracted fields.

1. Extraction Approach

File Input: Accepts .jpg, .jpeg, .png, and .pdf.

PDF Handling: PDF pages are converted to images using pdf2image.

OCR: Tesseract OCR extracts text from images.

Parsing: Regex is used to extract fields such as candidate name, subject marks, and issue date.

JSON Output:

candidate_details: Name, DOB, Exam Year

subject_marks: Subject, obtained/max marks, grade

overall_result: Pass/Fail, Division

issue_date: Date of issuance

2. Confidence Scoring

OCR Confidence: Average character-level confidence from Tesseract.

Heuristic Adjustments:

Fields matching expected patterns maintain high confidence.

Ambiguous or partially matched fields reduce confidence.

3. Design Choices

Framework: FastAPI for asynchronous request handling and OpenAPI documentation.

Deployment: Dockerized with tesseract-ocr and poppler-utils.

Error Handling:

Invalid file types → 400 Bad Request

OCR failures → 500 Internal Server Error

Optional Features: Multi-page PDFs, confidence scoring.

4. API Features

Accepts both image and PDF inputs.

Handles multiple requests concurrently.

Returns structured JSON with confidence scores.

Provides clear error messages for invalid input or OCR failure.

Optional: bounding boxes, batch processing, API authentication.

5. Project Setup

Dockerized deployment for easy setup.

Dependencies managed with requirements.txt.

FastAPI provides interactive API documentation for testing.

Secrets and credentials are kept outside the repository using environment variables.
