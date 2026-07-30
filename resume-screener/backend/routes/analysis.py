from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import shutil
import os
import json

from ai_handler import screen_resume
from pdf_utils import extract_text_from_pdf, extract_text_from_docx

router = APIRouter()


@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    
    if not job_description.strip():
        raise HTTPException(
        status_code=400,
        detail="Please enter a job description."
    )

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", resume.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    # Extract resume text
    if resume.filename.endswith(".pdf"):
        resume_text = extract_text_from_pdf(file_path)

    elif resume.filename.endswith(".docx"):
        resume_text = extract_text_from_docx(file_path)

    else:
        return {
            "error": "Only PDF and DOCX files are supported."
        }

    if not resume_text.strip():
            raise HTTPException(
            status_code=400,
            detail="Could not extract text from the uploaded resume."
        )
    
    # validation
    try:
        response = screen_resume(
            resume_text,
            job_description
        )

        try:
            return json.loads(response)

        except json.JSONDecodeError:
            raise HTTPException(
                status_code=500,
                detail="Gemini returned invalid JSON."
            )

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=str(e)
        )

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)