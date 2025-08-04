import re

def parse_resume_text(text):
    data = {}

    # Name (First line)
    lines = text.strip().splitlines()
    data['name'] = lines[0].strip() if lines else ""

    # Email
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    data['email'] = email_match.group(0) if email_match else None

    # Phone (India format or (xxx) xxx-xxxx)
    phone_match = re.search(r'(\+91\s*\d{10}|\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})', text)
    data['phone'] = phone_match.group(0) if phone_match else None

    # LinkedIn
    linkedin_match = re.search(r'linkedin\.com/in/[^\s]+', text)
    data['linkedin'] = linkedin_match.group(0) if linkedin_match else None

    # Summary (Basic)
    summary_keywords = ['career objective', 'summary']
    summary = ""
    for i, line in enumerate(lines):
        if any(k.lower() in line.lower() for k in summary_keywords):
            summary = " ".join(lines[i+1:i+4])
            break
    data['summary'] = summary.strip()

    return data
