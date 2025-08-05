import re

def extract_email(text):
    # Matches common email formats
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else None

def extract_phone(text):
    # Matches numbers with optional +, spaces, dashes, and parentheses
    match = re.search(r"(\+?\d{1,3})?[\s-]?\(?\d{2,4}\)?[\s-]?\d{3,5}[\s-]?\d{4}", text)
    return match.group(0) if match else None

def extract_linkedin(text):
    # Matches LinkedIn profile URLs
    match = re.search(r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+", text)
    return match.group(0) if match else None

def extract_name(text):
    # Avoid common header lines like "Resume" or "CV"
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    for line in lines:
        if line.lower() not in ("resume", "curriculum vitae", "cv"):
            return line
    return None

def parse_resume_sections(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "linkedin": extract_linkedin(text),
    }