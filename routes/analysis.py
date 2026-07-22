from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os

from pdf_utils import extract_text_from_pdf, extract_text_from_docx

router = APIRouter()


@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", resume.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    if resume.filename.endswith(".pdf"):
        resume_text = extract_text_from_pdf(file_path)

    elif resume.filename.endswith(".docx"):
        resume_text = extract_text_from_docx(file_path)

    else:
        return {
            "error": "Only PDF and DOCX files are supported."
        }

    return {
        "message": "Resume text extracted successfully.",
        "resume_text": resume_text,
        "job_description": job_description
    }