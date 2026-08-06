from fastapi import UploadFile
from PyPDF2 import PdfReader
import io

async def extract_document_text(file: UploadFile):
    file_bytes = await file.read()

    if file.filename.endswith(".txt"):
        return file_bytes.decode("utf-8") 

    elif file.filename.endswith(".pdf"):
        pdf=PdfReader(io.BytesIO(file_bytes))
        text = ""

        for page in pdf.pages:
            page_text= page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    else:
        raise ValueError("Only PDF and TXT files are supported.")        