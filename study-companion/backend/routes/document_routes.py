from fastapi import APIRouter, UploadFile, File, HTTPException
from services.document_service import extract_document_text

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a PDF or TXT file and extract its text.
    """

    if not (
        file.filename.endswith(".pdf")
        or file.filename.endswith(".txt")
    ):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are allowed."
        )

    extracted_text = await extract_document_text(file)

    return {
        "filename": file.filename,
        "message": "Document uploaded successfully.",
        "extracted_text": extracted_text
    }