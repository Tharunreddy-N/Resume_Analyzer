import os
import re
from pdfminer.high_level import extract_text as pdf_extract_text
from docx import Document

def clean_text(text):
    """Remove unwanted artifacts like (cid:###) from extracted text."""
    return re.sub(r'\(cid:\d+\)', '', text)

def extract_text_from_pdf(pdf_path):
    """Extract and clean text from a PDF file."""
    raw_text = pdf_extract_text(pdf_path)
    return clean_text(raw_text)

def extract_text_from_docx(docx_path):
    """Extract and clean text from a DOCX file."""
    doc = Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return clean_text(text)

def extract_text_from_txt(txt_path):
    """Extract and clean text from a TXT file."""
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return clean_text(text)

def extract_resume_text(file_path):
    """Detect file type and extract text accordingly."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    elif file_path.endswith(".txt"):
        return extract_text_from_txt(file_path)
    else:
        raise ValueError("Unsupported file type. Use PDF, DOCX, or TXT.")