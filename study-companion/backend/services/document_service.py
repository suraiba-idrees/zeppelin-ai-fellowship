from fastapi import UploadFile
from PyPDF2 import PdfReader
import io
import re


def clean_extracted_text(text: str) -> str:
    """
    Clean up whitespace artifacts (stray tabs, repeated spaces/newlines)
    that PyPDF2 sometimes introduces when extracting text from PDFs.
    """
    if not text:
        return text

    # Replace tab characters with a single space
    text = text.replace("\t", " ")

    # Collapse multiple spaces into one
    text = re.sub(r" {2,}", " ", text)

    # Collapse 3+ newlines into a max of 2 (keep paragraph breaks)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


async def extract_document_text(file: UploadFile):
    file_bytes = await file.read()

    if file.filename.endswith(".txt"):
        return file_bytes.decode("utf-8")

    elif file.filename.endswith(".pdf"):
        pdf = PdfReader(io.BytesIO(file_bytes))
        text = ""

        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return clean_extracted_text(text)

    else:
        raise ValueError("Only PDF and TXT files are supported.")