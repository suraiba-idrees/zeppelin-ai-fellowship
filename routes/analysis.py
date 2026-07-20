
from fastapi import APIRouter
from models.analysis import AnalysisRequest

router = APIRouter()

@router.post("/analyze")
def analyze_resume(data: AnalysisRequest):
    return {
        "message": "Analysis endpoint is ready.",
        "resume_text": data.resume_text,
        "job_description": data.job_description
    }