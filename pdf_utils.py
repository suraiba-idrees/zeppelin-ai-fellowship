"""
pdf_utils.py

Utility functions for extracting text from uploaded resume PDF files.
"""

import os
from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_pdf(pdf_file_path):
    """
    Extract text from a PDF file.

    Args:
        pdf_file_path (str): Path to the PDF file.

    Returns:
        str: The extracted text from the PDF.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a PDF or contains no readable text.
    """

    # Check if the file exists
    if not os.path.exists(pdf_file_path):
        raise FileNotFoundError(f"File not found: {pdf_file_path}")

    # Check if the file is a PDF
    if not pdf_file_path.lower().endswith(".pdf"):
        raise ValueError("Invalid file format. Please provide a PDF file.")

    try:
        reader = PdfReader(pdf_file_path)

        # Check if the PDF has any pages
        if len(reader.pages) == 0:
            raise ValueError("The PDF file is empty.")

        extracted_text = ""

        # Read text from each page
        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                extracted_text += page_text + "\n"

        # Check if any text was extracted
        if not extracted_text.strip():
            raise ValueError("No readable text found in the PDF.")

        return extracted_text

    except Exception as e:
        raise RuntimeError(f"Error while reading the PDF: {e}")




def extract_text_from_docx(docx_file_path):
    """
    Extract text from a DOCX file.

    Args:
        docx_file_path (str): Path to the DOCX file.

    Returns:
        str: The extracted text from the DOCX file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not DOCX or contains no readable text.
    """

    # Check if the file exists
    if not os.path.exists(docx_file_path):
        raise FileNotFoundError(f"File not found: {docx_file_path}")

    # Check file extension
    if not docx_file_path.lower().endswith(".docx"):
        raise ValueError("Invalid file format. Please provide a DOCX file.")

    try:
        document = Document(docx_file_path)

        extracted_text = ""

        # Extract text from paragraphs
        for paragraph in document.paragraphs:
            if paragraph.text:
                extracted_text += paragraph.text + "\n"

        # Check if text was extracted
        if not extracted_text.strip():
            raise ValueError("No readable text found in the DOCX file.")

        return extracted_text

    except Exception as e:
        raise RuntimeError(f"Error while reading the DOCX file: {e}")

