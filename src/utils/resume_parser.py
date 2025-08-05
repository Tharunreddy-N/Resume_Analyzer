# resume_parser.py

"""
Extracts structured data such as name, email, phone number, LinkedIn URL, and summary from raw resume text.
"""

import re

def parse_resume_text(text):
    data = {}

    # Split text into lines
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    # Extract name (skip common headers like "Resume", "Curriculum Vitae")
    for line in lines:
        if line.lower() not in ("resume", "curriculum vitae", "cv"):
            data['name'] = line
            break
    else:
        data['name'] = ""

    # Email extraction
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    data['email'] = email_match.group(0) if email_match else None

    # Phone extraction (India and US-style)
    phone_match = re.search(r'(\+91\s*\d{10}|\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})', text)
    data['phone'] = phone_match.group(0) if phone_match else None

    # LinkedIn URL
    linkedin_match = re.search(r'(https?://)?(www\.)?linkedin\.com/in/[^\s]+', text)
    data['linkedin'] = linkedin_match.group(0) if linkedin_match else None

    # Extract a basic summary based on keywords
    summary_keywords = ['career objective', 'summary']
    summary = ""
    for i, line in enumerate(lines):
        if any(k.lower() in line.lower() for k in summary_keywords):
            summary = " ".join(lines[i+1:i+4])
            break
    data['summary'] = summary.strip()

    return data
