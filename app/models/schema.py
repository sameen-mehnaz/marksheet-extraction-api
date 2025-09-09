from pydantic import BaseModel
from typing import List, Optional, Dict

class SubjectMark(BaseModel):
    subject: str
    max_marks: Optional[str]
    obtained_marks: Optional[str]
    grade: Optional[str]
    confidence: float

class ExtractionResponse(BaseModel):
    candidate_details: Dict[str, Dict[str, float]]  # e.g., {"name": {"value": "John Doe", "confidence": 0.95}}
    subject_marks: List[SubjectMark]
    overall_result: Dict[str, Dict[str, float]]
    issue_date: Optional[Dict[str, float]]
