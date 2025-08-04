from utils.resume_parser import parse_resume_text
from preprocessing.parser import extract_resume_text

def process_resume_file(file_path):
    raw_text = extract_resume_text(file_path)
    structured_data = parse_resume_text(raw_text)
    return structured_data