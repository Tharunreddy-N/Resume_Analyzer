import re

def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r"\+?\d[\d\s-]{8,}", text)
    return match.group(0) if match else None

def extract_linkedin(text):
    match = re.search(r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+", text)
    return match.group(0) if match else None

def extract_name(text):
    # Very basic heuristic (can be replaced with NER later)
    lines = text.split('\n')
    return lines[0].strip() if lines else None

def parse_resume_sections(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "linkedin": extract_linkedin(text),
    }