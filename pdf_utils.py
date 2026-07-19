"""
pdf_utils.py

Utility functions for extracting text from uploaded resume PDF files.
"""

import os
from PyPDF2 import PdfReader


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


#if __name__ == "__main__":
    #pdf_path = "Aniqa CV(v2).pdf"

    #try:
        #text = extract_text_from_pdf(pdf_path)
        #print(text)

    #except Exception as error:
        #print(error)