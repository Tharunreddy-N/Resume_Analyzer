# parser_pipeline.py

from utils.parser import extract_resume_text
from utils.cleaner import parse_resume_sections

def process_resume_file(file_path):
    """
    Given a file path to a resume, extract the text and parse contact info.
    Returns structured data containing name, email, phone, and LinkedIn.
    """
    raw_text = extract_resume_text(file_path)
    structured_data = parse_resume_sections(raw_text)
    return structured_data