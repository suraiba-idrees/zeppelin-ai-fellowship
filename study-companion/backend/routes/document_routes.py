from fastapi import APIRouter, UploadFile, File, HTTPException
from services.document_service import extract_document_text
from services.embedding_service import process_document
from services.qdrant_service import insert_chunks, create_collection

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a PDF or TXT file, extract its text, chunk it, generate
    embeddings, and store them in the Qdrant collection.
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

    if not extracted_text or not extracted_text.strip():
        raise HTTPException(
            status_code=400,
            detail="No text could be extracted from this file."
        )

    chunks_with_embeddings = process_document(extracted_text)

    create_collection()
    inserted_count = insert_chunks(chunks_with_embeddings)

    return {
        "filename": file.filename,
        "message": "Document uploaded, chunked, embedded, and stored successfully.",
        "chunks_stored": inserted_count
    }