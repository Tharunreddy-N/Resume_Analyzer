# helpers.py

import re

# Precompiled regex for email extraction
EMAIL_REGEX = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")

def extract_emails(text):
    """
    Extract all valid email addresses from the given text.
    
    Parameters:
        text (str): Input text to search for email addresses.
    
    Returns:
        List[str]: A list of extracted email addresses.
    """
    return EMAIL_REGEX.findall(text)